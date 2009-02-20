
ui: metaphor/metaphor.ui qrc
	pyuic4 metaphor/metaphor.ui -o metaphor/qtui.py
qrc: images/metaphor.qrc
	pyrcc4 images/metaphor.qrc -o metaphor/metaphor_rc.py