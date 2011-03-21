====================
django-flatpages-nav
====================


Overview
--------

This app helps any Django project easily control the order and visibility of flat page links in their main (usually header) and footer navs. The process from an end-users perspective is simple, add flatpages and then using Django admin control their visibility and order in the main/footer nav.

No need to ever hard-code these links in your base templates!


Installation
------------

- Install flatpages_nav (ideally in your virtualenv!) using pip or simply getting a copy of the code and putting it in a directory in your codebase.

- Add ``flatpages_nav`` to your Django settings ``INSTALLED_APPS``::
	
	INSTALLED_APPS = [
        # ...
        "flatpages_nav",
    ]

- Add ``nav_flatpages`` to your Django settings ``TEMPLATE_CONTEXT_PROCESSORS``::
	
	TEMPLATE_CONTEXT_PROCESSORS = [
		# ...
		"flatpages_nav.context_processors.nav_flatpages",
	]

- Run a db migration (using south) to make sure db table(s) for this app get created::
	
	``python manage.py migrate flatpages_nav``

- In your base template (usually base.html) use the new context variables that this app has added::
	
	``<ul id="main_nav">
        {% for flatpage in main_nav_flatpages %}
            <li><a href="{{ flatpage.url }}">{{ flatpage.title }}</a></li>
        {% endfor %}
    </ul>``
	
	and in the footer
	
	``<ul id="footer_nav">
        {% for flatpage in footer_nav_flatpages %}
            <li><a href="{{ flatpage.url }}">{{ flatpage.title }}</a></li>
        {% endfor %}
    </ul>``


This open-source app is brought to you by Tivix, Inc. ( http://tivix.com/ )
