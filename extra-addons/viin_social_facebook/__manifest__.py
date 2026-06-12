{
    'name': "Facebook Social Marketing",
    'name_vi_VN': "Facebook Social Marketing",

    'summary': """
Integrate the Social Marketing app with Facebook
""",

    'summary_vi_VN': """
Tích hợp ứng dụng Social Marketing với Facebook
""",

    'description': """
Demo video: `Facebook Social Marketing <https://youtu.be/1uGSRsZpT3o>`_

What it does
============
Facebook Social Marketing helps you create, preview, publish content, and seamlessly manage your presence on Facebook within the app. You can also easily get notified, engage with your audience, and respond to all comments, and messages directly from the Social Marketing app.

Key Features
============
#. See overall articles & posts on Facebook at a glance
#. Manage all content creation process on Facebook

   * Easily create content, attach files, preview and publish on LinkedIn
   * Track the progress of articles (Draft, Confirmed, Canceled) and who is assigned

#. Monitor online presence on Facebook

   * Post, edit, share and delete content
   * React, respond, delete, and hide comments
   * Receive notifications and messages across LinkedIn channel
   * Sync all Facebook posts into one database

Note
====
You need to successfully complete Business Verification and verify certain access permissions for your Facebook app before using this module. Some of the access permissions that need to be verified include:

#. pages_show_list
#. pages_read_engagement
#. pages_manage_posts
#. pages_read_user_content
#. pages_manage_engagement
#. pages_manage_metadata
#. pages_messaging (Optional messaging feature)

Supported Editions
==================
1. Community Edition

    """,

    'description_vi_VN': """
Demo video: `Facebook Social Marketing <https://youtu.be/1uGSRsZpT3o>`_

Mô tả
=====
Facebook Social Marketing giúp bạn tạo, xem trước các bài đăng, và quản lý hiệu quả nội dung trên Facebook mà không cần phải rời ứng dụng. Bạn cũng dễ dàng nhận thông báo, tương tác với người dùng, trả lời bình luận và tin nhắn ngay trong ứng dụng Social Marketing.

Tính năng nổi bật
=================
#. Trực quan hoá tất cả các bài viết và bài đã đăng trên Facebook
#. Đơn giản hoá quá trình lên nội dung trên Facebook

   * Dễ dàng sáng tạo nội dung, đính kèm file, xem trước và đăng tải bài viết
   * Kiểm tra tiến độ bài viết: dự thảo, đã xác nhận, đã huỷ và ai đang đảm nhiệm bài biết này

#. Kiểm soát nội dung trên Facebook

   * Đăng, sửa, chia sẻ và xoá nội dung
   * Tương tác, trả lời, xoá và ẩn bình luận
   * Trả lời tin nhắn và nhận thông báo trên trang Facebook
   * Đồng bộ hoá tất cả các bài đã đăng, thông báo lên hệ thống

Lưu ý
=====
Bạn cần xác minh doanh nghiệp và xác minh một số quyền truy cập thành công cho ứng dụng Facebook của bạn mới có thể sử dụng module này. Một số quyền truy cập cần xác minh:

#. pages_show_list
#. pages_read_engagement
#. pages_manage_posts
#. pages_read_user_content
#. pages_manage_engagement
#. pages_manage_metadata
#. pages_messaging (tính năng tin nhắn, tùy chọn)

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com/apps/app/17.0/viin_social_facebook",
    'live_test_url': "https://v17demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v17demo-vn.viindoo.com",
    'demo_video_url': "https://youtu.be/1uGSRsZpT3o",
    'support': "apps.support@viindoo.com",
    'category': 'Marketing/Social Marketing',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['viin_social'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/media_data.xml',
        'data/ir_config_parameter_data.xml',
        'views/res_config_settings_views.xml',
        'views/social_media_views.xml',
        'views/social_page_views.xml',
        'views/social_article_views.xml',
        'views/social_post_views.xml',
        'views/social_facebook_preview_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'viin_social_facebook/static/src/scss/*'
        ],
    },
    'images': [
        'static/description/main_screenshot.png'
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'auto_install': True,
    'price': 198.9,
    'subscription_price': 9.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
