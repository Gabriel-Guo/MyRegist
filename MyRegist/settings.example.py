# python 3.6
# -*- coding: utf-8 -*-
# @Time    : 2020-01-27 00:35
# @Author  : 乐天派逗逗
# @Site    : Windows 10
# @File    : settings.example.py.py
# @Software: PyCharm
# @Contact : 1584838420@qq.com
# @Features:

"""
Django settings for MyRegist project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^swt^d@5f8)=f)pty7s)(cegg2dbwd-#i4__dpadc7eo8kb782'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'captcha'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyRegist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyRegist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'       # 中文'en-us'

TIME_ZONE = 'Asia/Shanghai'     # 北京时间 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# 邮件发送
# 特别说明：
# 某些邮件公司可能不开放smtp服务
# 某些公司要求使用ssl安全机制
# 某些smtp服务对主机名格式有要求
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'       # 指定发送邮件的后端模块，大多数情况下照抄！
# EMAIL_HOST = 'smtp.sina.com'                                        # 发送方的smtp服务器地址，建议使用新浪家的；
# EMAIL_PORT = 25                                                     # smtp服务端口，默认为25；
# EMAIL_HOST_USER = 'your email@qq.com'                                    # 你在发送服务器的用户名；
# EMAIL_HOST_PASSWORD = 'xxxxxxxx'                                 # 对应用户的密码。


# 邮件配置
# Host for sending email.
EMAIL_HOST = 'smtp.qq.com'                 # 发送方的smtp服务器地址

# Port for sending email.
EMAIL_PORT = 587                           # smtp服务端口

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'your email@qq.com'       # 发送方 邮箱地址
EMAIL_HOST_PASSWORD = 'xxxxxxxx'   # 获得的  授权码
EMAIL_USE_TLS = True                       # 必须为True
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None

# Default email address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = 'your email@qq.com'  # 和 EMAIL_HOST_USER  相同

# 注册有效期天数
CONFIRM_DAYS = 7
