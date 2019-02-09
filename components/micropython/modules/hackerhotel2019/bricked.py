import audio, time, appglue, easydraw, badge

brick = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xcb\x00\x00\x00\x80\x01\x03\x00\x00\x00\x9f\xaa\x0f\xdf\x00\x00\x00\x06PLTE\xff\xff\xff\x00\x00\x00U\xc2\xd3~\x00\x00\x00\tpHYs\x00\x00\x0e\xc4\x00\x00\x0e\xc4\x01\x95+\x0e\x1b\x00\x00\x01\xdeIDATH\x89\xe5\xd6\xcd\x8d\xdb0\x10\x05\xe0Qd@\xb7\xa8\x81 ,E[JJH\x01\x01\xc8\xd2X\x8aJ\xe0\xd1\x07C\xb332E\xf1g\xde}\xb1!l@\xe0\x07S\xa3G\xdb\x1c\xa2fL\xf2\xfeA\xe6\x98"\xd1O@\x87\xbelb\xe6\xff\x87\xa6\xa0\xf1\t=GJD\xbfic\xde\x8d\xb5\x9e\xfe\xa0\x85Y\x93\x7fX\xb7Yh\x8eD\xbf\xec\n\xe6\x83\xe6\x17 \xb9\xf8r\x14d\x82\xae\x99\x96$\xa3U3J#q\x98\x99V\xe6\x10\xf2\xcaO\x9a\xf6L2\x88\xb6\x9d\xf6\xbcr\xa2\xb5!\x19R\x87\xd7\x95\x03\xf9\x9e\xce\x0b\xd9\x03\xd9\x01\x93txH3Cr\x98\x18\xd2rR\xc83GM\xfe\xa4\xa8\x0f\xe9\xafh\xde\xa4Q\t\xc9\xd4\xa6wMu,o\xca\x0f\xc9\xf4\xa1;\xe0ue\r\xb1\x90\x8e\xbf\xb2Pp\x9a\xac\xeb\xc9Kn\xb2\x01\x1c\xcf\xa9\x96XS]\xd3Y\xb9E\xf9\xc2\xa6\xfc!\x8b6H\x13Cr7\x95\x8c2\xf1M%\xa3\\|Es.9\x93\xafH\x7f\x84\x7f\xf4G\xbei|\x0b\xd7$\xe3\x9f|y\xc3\xa2+o=\xf9\xc3\x9dk\xbd7\xaa\xa5+#\x87\xc9C\xaa\x8a\xe8\xc9C\xaa\x8b\xe8\xc8A\x9a\x18\xd2\x8a\xa8\xca\xbc&\xd7\xc5W\xd1\x19\x9f7\xa9\x8f\xaf\xa6\xea\xdb2\xd2\xd4\xcbM\x0e\xd3 \x85VL}\xe57\xf5\x8f\xfb\x9d)@\xba\xfe\xce\r\xda!\x95cv\xa4\x84)@\xba\xcf\x94\x81vH\xd5Y\xdfS\xc2\x14 \xd5\'eG\x11R\xd3p\xb4\x940\x05H\xedq\xddP\xc4D\x90\x9e\x98"\xa4\xbe\x8b\xaa(a\n\x90\x86\xd6\xeb\xa6\x08il\xe5\n\xf5ET4H\xa1\xb1\xff+4\x14Q\xc8j5\xcb\xa1\n\xc9\x90LF\x11\x17\x19Ed\xb2\xfb\xdd\xc5N\xa2P\x80\xf42%\xb79\x90lQ2\x1f\xeaM\x11\x12(\x82\xee\x96\xcf"$\xb4\xa0"\x84\x02\xa4\x875\xf9\t\n0\xc6\x08\xe3\xac\xc4H\x00\x00\x00\x00IEND\xaeB`\x82'

info = badge.png_info(brick)
x = int((ugfx.width()-info[0])/2)

while True:
	ugfx.clear()
	badge.png(x,0,brick)
	ugfx.flush()
	audio.play_mp3_file("/media/icq.mp3")
	time.sleep(2)
	try:
		badge.i2c_read_reg(0x5a, 0x00, 0x01) # Test the i2c connection
		appglue.home()
	except:
		pass
	easydraw.msg("I2C ERROR","ERROR",True)
	easydraw.msg("Remove your add-ons!")
	time.sleep(2)
