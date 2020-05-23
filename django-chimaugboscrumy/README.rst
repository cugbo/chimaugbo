===============
chimaugboscrumy
===============
chimaugboscrumy is a simple django app to conduct web-based test
for linuxjobber internship students, where they will be rated after taking a task and submitting
Detailed documentation is in the "docs" directory

Quick Start
===========
1. Add "chimaugboscrumy" to your INSTALLED_APPS settings like this::
    INSTALLED_APPS = [
        ...
        'chimaugboscrumy',
    ]
2. Include the chimaugboscrumy URLconf in your projrct urls.py like this::
        path ('chimaugboscrumy/', include ('chimaugboscrumy.urls')),
3. Run 'python manage.py migrate' to create the chimaugboscrumy models
4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a chimaugboscrumy (you'll need the Admin app enabled)
5. Visit http://127.0.0.1:8000/chimaugboscrumy/ to participate in the test

