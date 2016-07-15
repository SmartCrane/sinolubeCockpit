# -*- coding: UTF-8 -*-
"""
Django settings for Sinolube_cockpit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,logging
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ql73iy!ty&r$d)oc0vs7-#zho9d(%fwuipe**@t9ejqi7#_whh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cockpit',
    # 'OCEtl',
    'Sinolube_cockpit',
    # todo 部署时启用
    # 'django_crontab',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Sinolube_cockpit.urls'

WSGI_APPLICATION = 'Sinolube_cockpit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

'''
部署开发、测试、生产服务器，需要修改NAME & HOST
'''
DATABASES = {
    # ---------------开发配置-----------------------------------
    # DW
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'lube_vis_data',
    #     'USER': 'lube_vis_data',
    #     'PASSWORD': 'Q1W2e3r4',
    #     # 开发库
    #     'HOST': 'rds5f96121j95l3n685e.mysql.rds.aliyuncs.com',
    #
    #     #测试库
    #     # 'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     # 生产库
    #     # 'HOST': 'rm-z1kv2ks52r58m91m7.mysql.rds.aliyuncs.com',
    #
    #     'PORT': '3306',
    # },
    # # 订单
    # 'OC': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop3',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # # 仓储
    # 'WCS': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop5',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # # 调运
    # 'TC': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop2',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # # 订单预警
    # 'ALARM': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop7',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # #主数据
    # 'MDM': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop1',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # #评价中心
    # 'EVAL': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop6',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # ---------------测试配置-----------------------------------
    # DW
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_lube_vis_data',
    #     'USER': 'lube_vis_data',
    #     'PASSWORD': 'Q1W2e3r4',
    #     # 开发库
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # # 订单
    # 'OC': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop3',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # # 仓储
    # 'WCS': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop5',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # # 调运
    # 'TC': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop2',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # # 订单预警
    # 'ALARM': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop7',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # #主数据
    # 'MDM': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop1',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    # #评价中心
    # 'EVAL': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 'ENGINE': 'mysql.connector.django',
    #     'NAME': 'uat_loop6',
    #     'USER': 'loop_vis_read',
    #     'PASSWORD': 'Lsd_160602',
    #     'HOST': 'rm-z1kc18rme4ffde7oc.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # },
    #---------------生产配置----------------------------------
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': 'prd_lube_vis_data',
        'USER': 'bHViZV92aXNfZGF0YQ==',
        'PASSWORD': 'YWxvbWNfTDE4NTU=',
        'HOST': 'rm-z1kv2ks52r58m91m7.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    },
    # 订单
    'OC': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': 'prd_loop3',
        'USER': 'bG9vcF92aXNfcmVhZA==',
        'PASSWORD': 'bWFncmVOMDYwNV8=',
        'HOST': 'rm-z1kv2ks52r58m91m7.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    },
    # 仓储
    'WCS': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': 'prd_loop5',
        'USER': 'bG9vcF92aXNfcmVhZA==',
        'PASSWORD': 'bWFncmVOMDYwNV8=',
        'HOST': 'rm-z1kv2ks52r58m91m7.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    },
    # 调运
    'TC': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': 'prd_loop2',
        'USER': 'bG9vcF92aXNfcmVhZA==',
        'PASSWORD': 'bWFncmVOMDYwNV8=',
        'HOST': 'rm-z1kv2ks52r58m91m7.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    },
    # 订单预警
    'ALARM': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': 'prd_loop7',
        'USER': 'bG9vcF92aXNfcmVhZA==',
        'PASSWORD': 'bWFncmVOMDYwNV8=',
        'HOST': 'rm-z1kv2ks52r58m91m7.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    },
    # 主数据
    'MDM': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': 'prd_loop1',
        'USER': 'bG9vcF92aXNfcmVhZA==',
        'PASSWORD': 'bWFncmVOMDYwNV8=',
        'HOST': 'rm-z1kv2ks52r58m91m7.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    },
    # 评价中心
    'EVAL': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'mysql.connector.django',
        'NAME': 'prd_loop6',
        'USER': 'bG9vcF92aXNfcmVhZA==',
        'PASSWORD': 'bWFncmVOMDYwNV8=',
        'HOST': 'rm-z1kv2ks52r58m91m7.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    },
}
DATABASE_ROUTERS = [
    'OCEtl.router.OCETLProjectRouter',
    'WCSEtl.router.WCSETLProjectRouter',
    'TCEtl.router.TCETLProjectRouter',
    'ALARMEtl.router.ALARMETLProjectRouter',
    'MDMEtl.router.MDMETLProjectRouter',
    'evalEtl.router.EVALETLProjectRouter'
]

CRONJOBS = [
    ('0 * * * *', 'cockpit_oc_wcs_tc_etl','> /tmp/oc_wcs_tc_scheduled_job.log'),
    ('0 * * * *', 'cockpit_alarm_etl','> /tmp/alarm_scheduled_job.log'),
    ('0 * * * *', 'cockpit_logeva_etl','> /tmp/logeva_scheduled_job.log'),
    # 0 * * * * /usr/bin/python2.7 /usr/local/Sinolube_cockpit/manage.py cockpit_oc_wcs_tc_etl > /tmp/oc_wcs_tc_scheduled_job.log
    # 0 * * * * /usr/bin/python2.7 /usr/local/Sinolube_cockpit/manage.py cockpit_alarm_etl > /tmp/alarm_scheduled_job.log
    # 0 * * * * /usr/bin/python2.7 /usr/local/Sinolube_cockpit/manage.py cockpit_alarm_etl > /tmp/alarm_scheduled_job.log
    # 0 * * * * /usr/bin/python2.7 /usr/local/Sinolube_cockpit/manage.py cockpit_logeva_etl > /tmp/logeva_scheduled_job.log
]
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

