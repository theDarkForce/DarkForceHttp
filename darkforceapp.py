# -*- coding: UTF-8 -*-
# darkforce
# create at 2015/6/15
# autor: qianqians

import sys
import pymongo
import globalv
from loginui import *
sys.path.append('../plask/')
from plask import *

def create_title(cname, name, praframe):
	title = pytext(cname, name, pyhtmlstyle.float_left, praframe)
	title.set_size(130, 0)
	title.set_font_size(200)
	title.set_border_style(pyhtmlstyle.solid)
	title.set_border_color((150, 150, 150))
	title.set_border_size(1)
	ev = uievent('http://127.0.0.1:5000/', title, pyelement.onmouseover)
	ev.add_call_ui(title.client_set_background_color((210,210,210)))
	ev.add_call_ui(title.client_set_cursor(pyhtmlstyle.pointer))
	title.register_uievent(ev)
	evo = uievent('http://127.0.0.1:5000/', title, pyelement.onmouseout)
	evo.add_call_ui(title.client_set_background_color((255,255,255)))
	evo.add_call_ui(title.client_set_cursor(pyhtmlstyle.auto))
	title.register_uievent(evo)

	return title

def layout():
	conn = pymongo.Connection('localhost',27017)
	db = conn.darkforce
	globalv.collection_user = db.user
	globalv.collection_file = db.file
	globalv.collection_text = db.text

	app = plaskapp('0.0.0.0', 5000)

	p = pypage('darkforce', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_auto)
	p.add_page_route('/')

	titleui(p)

	c = pycontainer('title', pyhtmlstyle.margin_auto, p)
	c.set_location(450, 0)
	c.set_size(656, 0)
	c.set_newline()

	titleh = create_title("首页", "home", c)
	titlep = create_title('产品', "product", c)
	titlet = create_title('教育', "technology", c)
	titleo = create_title('开源', "opensrc", c)
	titlea = create_title('关于我们', "aboutus", c)

	ch = pycontainer('text_home', pyhtmlstyle.margin_auto, p)
	ch.set_location(450, 20)
	ch.set_border_style(pyhtmlstyle.solid)
	ch.set_top_border_style(pyhtmlstyle.none)
	ch.set_visibility(True)
	ch.set_border_color((150, 150, 150))
	ch.set_border_size(1)
	ch.set_size(654, 80)

	ev = uievent('http://127.0.0.1:5000/', titleh, pyelement.onclick)
	ev.add_call_ui(ch.server_set_visible(False))
	titleh.register_uievent(ev)

	cp = pycontainer('text_product', pyhtmlstyle.margin_auto, p)
	cp.set_location(450, 20)
	cp.set_border_style(pyhtmlstyle.solid)
	cp.set_top_border_style(pyhtmlstyle.none)
	cp.set_visibility(False)
	cp.set_border_color((150, 150, 150))
	cp.set_border_size(1)
	cp.set_size(654, 80)

	ev = uievent('http://127.0.0.1:5000/', titlep, pyelement.onclick)
	ev.add_call_ui(cp.server_set_visible(False))
	titlep.register_uievent(ev)

	ct = pycontainer('text_technology', pyhtmlstyle.margin_auto, p)
	ct.set_location(450, 20)
	ct.set_border_style(pyhtmlstyle.solid)
	ct.set_top_border_style(pyhtmlstyle.none)
	ct.set_visibility(False)
	ct.set_border_color((150, 150, 150))
	ct.set_border_size(1)
	ct.set_size(654, 80)

	ev = uievent('http://127.0.0.1:5000/', titlet, pyelement.onclick)
	ev.add_call_ui(ct.server_set_visible(False))
	titlet.register_uievent(ev)

	co = pycontainer('text_opensrc', pyhtmlstyle.margin_auto, p)
	co.set_location(450, 20)
	co.set_border_style(pyhtmlstyle.solid)
	co.set_top_border_style(pyhtmlstyle.none)
	co.set_visibility(False)
	co.set_border_color((150, 150, 150))
	co.set_border_size(1)
	co.set_size(654, 80)

	ev = uievent('http://127.0.0.1:5000/', titleo, pyelement.onclick)
	ev.add_call_ui(co.server_set_visible(False))
	titleo.register_uievent(ev)

	ca = pycontainer('text_aboutus', pyhtmlstyle.margin_auto, p)
	ca.set_location(450, 20)
	ca.set_border_style(pyhtmlstyle.solid)
	ca.set_top_border_style(pyhtmlstyle.none)
	ca.set_visibility(False)
	ca.set_border_color((150, 150, 150))
	ca.set_border_size(1)
	ca.set_size(654, 80)

	ev = uievent('http://127.0.0.1:5000/', titlea, pyelement.onclick)
	ev.add_call_ui(ca.server_set_visible(False))
	titlea.register_uievent(ev)

	p.init()
	
	app.run()

if __name__ == '__main__':
	layout()
