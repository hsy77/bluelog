# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import random

from faker import Faker
from sqlalchemy.exc import IntegrityError

from bluelog.extensions import db
from bluelog.models import Admin, Category, Post, Comment, Link

fake = Faker("zh_CN")


def fake_admin():
    admin = Admin(
        username='admin',
        blog_title='博客',
        blog_sub_title="写下你的感悟。",
        name='思悟',
        about='思世间之大，悟人生变换。'
    )
    admin.set_password('helloflask')
    db.session.add(admin)
    db.session.commit()


def fake_categories(count=10):
    category1 = Category(name='新冠疫情')
    db.session.add(category1)
    category2 = Category(name='健康')
    db.session.add(category2)
    category3 = Category(name='体育')
    db.session.add(category3)
    category5 = Category(name='经济')
    db.session.add(category5)
    category6 = Category(name='军事')
    db.session.add(category6)
    category7 = Category(name='艺术')
    db.session.add(category7)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

# path="D:/这学期/云计算/云计算项目/bluelog"
path=""
def fake_posts(count=15):
    f1 = open(path+"/root/content/文本/content.txt", "r", encoding="utf-8")
    content1 = f1.readlines()
    f2 = open(path+"/root/content/文本/title.txt", "r", encoding="utf-8")
    head1 = f2.readlines()

    # f3 = open(path+"/root/content/健康/content.txt", "r", encoding="utf-8")
    # content2 = f3.readlines()
    # f4 = open(path+"/root/content/健康/title.txt", "r", encoding="utf-8")
    # head2 = f4.readlines()

    f5 = open(path+"/root/content/体育/content.txt", "r", encoding="utf-8")
    content3 = f5.readlines()
    f6 = open(path+"/root/content/体育/title.txt", "r", encoding="utf-8")
    head3 = f6.readlines()

    # f7 = open("C:/Users/12293/Desktop/程序员/content.txt", "r", encoding="utf-8")
    # content4 = f7.readlines()
    # f8 = open("C:/Users/12293/Desktop/程序员/title.txt", "r", encoding="utf-8")
    # head4 = f8.readlines()

    f9 = open(path+"/root/content/经济/content.txt", "r", encoding="utf-8")
    content5 = f9.readlines()
    f10 = open(path+"/root/content/经济/title.txt", "r", encoding="utf-8")
    head5 = f10.readlines()

    f11 = open(path+"/root/content/军事/content.txt", "r", encoding="utf-8")
    content6 = f11.readlines()
    f12 = open(path+"/root/content/军事/title.txt", "r", encoding="utf-8")
    head6 = f12.readlines()

    f13 = open(path+"/root/content/艺术/content.txt", "r", encoding="utf-8")
    content7 = f13.readlines()
    f14 = open(path+"/root/content/艺术/title.txt", "r", encoding="utf-8")
    head7 = f14.readlines()
    for i in range(count):
        post1 = Post(
            title=head1[i][:-19],
            body=content1[i],
            category=Category.query.get(1),
            timestamp=fake.date_time_this_year()
        )
        # post2 = Post(
        #     title=head2[i],
        #     body=content2[i],
        #     category=Category.query.get(2),
        #     timestamp=fake.date_time_this_year()
        # )
        post3 = Post(
            title=head3[i][:-19],
            body=content3[i],
            category=Category.query.get(3),
            timestamp=fake.date_time_this_year()
        )
        # post4 = Post(
        #     title=head4[i],
        #     body=content4[i],
        #     category=Category.query.get(4),
        #     timestamp=fake.date_time_this_year()
        # )
        post5 = Post(
            title=head5[i][:-19],
            body=content5[i],
            category=Category.query.get(4),
            timestamp=fake.date_time_this_year()
        )
        post6 = Post(
            title=head6[i][:-19],
            body=content6[i],
            category=Category.query.get(5),
            timestamp=fake.date_time_this_year()
        )
        post7 = Post(
            title=head7[i][:-19],
            body=content7[i],
            category=Category.query.get(6),
            timestamp=fake.date_time_this_year()
        )

        db.session.add(post1)
        # db.session.add(post2)
        db.session.add(post3)
        # db.session.add(post4)
        db.session.add(post5)
        db.session.add(post6)
        db.session.add(post7)
    db.session.commit()
    # for i in range(count):
    #     post = Post(
    #         title=fake.sentence(),
    #         body=fake.text(2000),
    #         category=Category.query.get(random.randint(1, Category.query.count())),
    #         timestamp=fake.date_time_this_year()
    #     )
    #     print(type(fake.sentence()),type(fake.text(2000)))
    #     print(fake.sentence(),fake.text(2000))
    #
    #     db.session.add(post)
    # db.session.commit()


def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

    salt = int(count * 0.1)
    for i in range(salt):
        # unreviewed comments
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=False,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

        # from admin
        comment = Comment(
            author='Mima Kirigoe',
            email='mima@example.com',
            site='example.com',
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            from_admin=True,
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()

    # replies
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            replied=Comment.query.get(random.randint(1, Comment.query.count())),
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()


def fake_links():
    twitter = Link(name='Twitter', url='#')
    facebook = Link(name='Facebook', url='#')
    linkedin = Link(name='LinkedIn', url='#')
    google = Link(name='Google+', url='#')
    db.session.add_all([twitter, facebook, linkedin, google])
    db.session.commit()
