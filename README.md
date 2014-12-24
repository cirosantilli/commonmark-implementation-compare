# CommonMark Implementation Compare

Compare compliance and speed of Markdown implementations against the CommonMark standard.

Note that each test does a system call to a library wrapper and feeds stdin, which leads to a big library loading overhead that might not be present in your application.

The main test file is [main.py](main.py). Get usage information with `./main.py -h`.

A [Vagrantfile](Vagrantfile) is provided and provisioned by [provision.sh](provision.sh), which contains the full installation procedure for the latests stable version of each compiler. Make sure to install Vagrant directly from the official website: Ubuntu repositories are too old. Vagrant usage is not mandatory: as long as the executables and libraries are installed in their PATHs, you can run the tests directly on your machine.

If compilers have options that make the output more compliant, those may be used. The only requirement is that a single set of options be used for all tests.

This repository will be Git tagged with the same Git tag as the CommonMark version used.

More information at: [README2.md](README2.md).

Test summary:

    Compiler id | Total time | Total errors | Error percent

    blackfriday     2.1222s  235  46%
    cmark           1.9516s    1   0%
    commonmarkjs   37.4651s    2   0%
    hoedown         1.8875s  221  43%
    kramdown       94.6460s  247  48%
    markdown2      28.9707s  278  54%
    markdown_pl    14.6919s  287  56%
    markdownjs     40.3337s  302  59%
    marked         35.3758s  258  50%
    maruku         87.1664s  316  61%
    multimarkdown   2.0579s  239  46%
    pandoc          6.3442s  268  52%
    peg_markdown    2.6402s  211  41%
    rdiscount      42.0547s  200  39%
    redcarpet      43.6608s  229  44%
    showdown       45.0655s  285  55%

Full output of `./main.py`:

    Disabled compilers:              gfm
    Enabled compilers not available: lunamark

    1 blackfriday
    2 cmark
    3 commonmarkjs
    4 hoedown
    5 kramdown

    6 markdown2
    7 markdown_pl
    8 markdownjs
    9 marked
    10 maruku

    11 multimarkdown
    12 pandoc
    13 peg_markdown
    14 rdiscount
    15 redcarpet

    16 showdown

    Test results | Test number | Start line | End line | Failed tests | Section

    .....  ..F.F  .F...  . | 1 249 254 3 Tab expansion
    .....  ..F.F  .F...  . | 2 256 263 3 Tab expansion
    .....  .....  .....  . | 3 280 288 0 Precedence
    .....  FFFF.  .FF..  F | 4 318 326 7 Horizontal rules
    .....  .....  .....  . | 5 330 334 0 Horizontal rules
    ...F.  .....  ...F.  . | 6 336 340 2 Horizontal rules
    F..FF  ....F  F....  . | 7 344 352 5 Horizontal rules
    .....  .....  ..F..  . | 8 356 364 1 Horizontal rules
    .....  ..F.F  .F...  . | 9 368 373 3 Horizontal rules
    .....  FFFF.  F....  F | 10 375 381 6 Horizontal rules
    .....  .....  .....  . | 11 385 389 0 Horizontal rules
    .....  .....  .....  . | 12 393 397 0 Horizontal rules
    .....  .....  .....  . | 13 399 403 0 Horizontal rules
    .....  FF...  .....  F | 14 405 409 3 Horizontal rules
    .....  F....  .....  . | 15 413 417 1 Horizontal rules
    F...F  ..FFF  F....  . | 16 421 431 6 Horizontal rules
    .....  F..FF  .....  . | 17 437 441 3 Horizontal rules
    F..FF  .....  .FF.F  . | 18 445 457 6 Horizontal rules
    ....F  ....F  FFF..  . | 19 461 469 5 Horizontal rules
    ....F  ...FF  FF...  F | 20 477 484 6 Horizontal rules
    F..FF  .....  .FF.F  . | 21 489 501 6 Horizontal rules
    F..F.  FFFFF  ..F.F  F | 22 505 515 10 Horizontal rules
    ....F  ...FF  FF...  F | 23 532 546 6 ATX headers
    ...FF  FFFFF  FFFFF  F | 24 550 554 13 ATX headers
    ...FF  FFFFF  FFFFF  F | 25 562 566 13 ATX headers
    .....  .....  .....  . | 26 570 574 0 ATX headers
    ....F  ...FF  FF...  F | 27 578 582 6 ATX headers
    ....F  ...FF  FF...  F | 28 586 590 6 ATX headers
    F..FF  FFFFF  FFFFF  F | 29 594 602 14 ATX headers
    .....  ..F.F  .F...  . | 30 606 611 3 ATX headers
    .....  ...F.  .....  . | 31 613 619 1 ATX headers
    F..FF  FFFFF  FFFFF  F | 32 623 629 14 ATX headers
    ....F  ...FF  FF...  F | 33 633 639 6 ATX headers
    F..FF  FF.FF  FF.FF  F | 34 643 647 12 ATX headers
    ....F  ...FF  FF...  F | 35 653 657 6 ATX headers
    F..FF  FFFFF  FFFFF  F | 36 661 665 14 ATX headers
    F..FF  FFFFF  FFFFF  F | 37 670 678 14 ATX headers
    ....F  ...FF  FFF..  F | 38 683 691 7 ATX headers
    ....F  ...FF  FF...  F | 39 693 701 6 ATX headers
    F..FF  FF.FF  FFFFF  F | 40 705 713 13 ATX headers
    ....F  ..FFF  FF...  F | 41 738 747 7 Setext headers
    ....F  ..FFF  FF...  F | 42 751 760 7 Setext headers
    F..FF  FFFFF  FFFFF  F | 43 765 778 14 Setext headers
    ....F  FFF.F  .F...  F | 44 782 795 7 Setext headers
    F..FF  FFFFF  FFF.F  F | 45 800 805 13 Setext headers
    F...F  ..FFF  F....  . | 46 809 815 6 Setext headers
    ....F  ....F  FFF..  . | 47 819 830 5 Setext headers
    ....F  ...FF  FF...  F | 48 834 839 6 Setext headers
    F...F  ...FF  FF...  F | 49 843 848 7 Setext headers
    F...F  FF.FF  FFFF.  F | 50 853 866 11 Setext headers
    F..FF  FFFF.  FFFFF  F | 51 871 879 13 Setext headers
    F..FF  FFFF.  FFFFF  F | 52 881 889 13 Setext headers
    F..FF  FF.FF  FFFFF  F | 53 893 908 13 Setext headers
    ....F  ..FFF  FFF..  F | 54 912 924 8 Setext headers
    ...F.  .....  ...F.  . | 55 928 933 2 Setext headers
    .....  FFFF.  .FF..  F | 56 939 945 7 Setext headers
    F..FF  FFFF.  FFFFF  F | 57 947 955 13 Setext headers
    ....F  FFF.F  .F...  F | 58 957 964 7 Setext headers
    F..FF  FFFF.  FFFFF  F | 59 966 974 13 Setext headers
    ....F  FFFFF  FF.F.  F | 60 979 984 10 Setext headers
    .....  ..F.F  .F...  . | 61 1001 1008 3 Indented code blocks
    .....  ..F.F  .F...  . | 62 1012 1023 3 Indented code blocks
    .....  ..F.F  .F...  . | 63 1027 1044 3 Indented code blocks
    .....  ..F.F  .F...  . | 64 1049 1058 3 Indented code blocks
    .....  .....  .....  . | 65 1063 1070 0 Indented code blocks
    ....F  ..F.F  .F...  . | 66 1076 1083 4 Indented code blocks
    ....F  FFFFF  FF...  F | 67 1088 1103 9 Indented code blocks
    .....  ..F.F  .F...  . | 68 1107 1114 3 Indented code blocks
    .....  ..F.F  .F...  . | 69 1119 1128 3 Indented code blocks
    .....  .....  .....  . | 70 1132 1137 0 Indented code blocks
    ...FF  FFF.F  .FF.F  . | 71 1186 1195 9 Fenced code blocks
    ...F.  FFF.F  FFF.F  F | 72 1199 1208 10 Fenced code blocks
    ...FF  FFF.F  .FF.F  . | 73 1213 1222 9 Fenced code blocks
    ...F.  FFF.F  FFF.F  F | 74 1224 1233 10 Fenced code blocks
    F..FF  FFFFF  FFF.F  F | 75 1237 1246 13 Fenced code blocks
    ...F.  FFF.F  FFF.F  F | 76 1248 1257 10 Fenced code blocks
    F..FF  FFFFF  FFFFF  F | 77 1261 1265 14 Fenced code blocks
    F..FF  FFFFF  FFFFF  F | 78 1267 1277 14 Fenced code blocks
    ...FF  FFF.F  ..FFF  . | 79 1281 1290 9 Fenced code blocks
    ...FF  FFFFF  ..FFF  F | 80 1294 1299 11 Fenced code blocks
    F..FF  FFFFF  FFFFF  F | 81 1305 1314 14 Fenced code blocks
    ...FF  FFF.F  .FFFF  F | 82 1316 1327 11 Fenced code blocks
    F..FF  FFFFF  FFFFF  F | 83 1329 1340 14 Fenced code blocks
    .....  ..F.F  .F...  . | 84 1344 1353 3 Fenced code blocks
    ...FF  FFF.F  .FF.F  F | 85 1358 1365 10 Fenced code blocks
    ...FF  FFF.F  .FFFF  F | 86 1367 1374 11 Fenced code blocks
    F..FF  FFFFF  FFFFF  F | 87 1378 1386 14 Fenced code blocks
    F....  ..FF.  FFF..  . | 88 1391 1397 6 Fenced code blocks
    F..FF  FFFFF  FFFFF  F | 89 1399 1407 14 Fenced code blocks
    ...FF  FFF.F  FFFFF  . | 90 1412 1423 11 Fenced code blocks
    ...FF  FFFFF  FFF.F  F | 91 1428 1440 12 Fenced code blocks
    ...FF  FFFFF  FFFFF  F | 92 1447 1458 13 Fenced code blocks
    F..FF  FFFFF  FFFFF  F | 93 1460 1471 14 Fenced code blocks
    ...FF  FFFFF  FFFFF  F | 94 1473 1478 13 Fenced code blocks
    .....  ..F..  .....  . | 95 1482 1488 1 Fenced code blocks
    ...FF  FFF.F  FFFFF  . | 96 1492 1499 11 Fenced code blocks
    .....  ..F..  .F...  . | 97 1527 1546 2 HTML blocks
    F..FF  FFFFF  FFFFF  F | 98 1548 1556 14 HTML blocks
    F..FF  FFFFF  F.FFF  F | 99 1560 1570 13 HTML blocks
    F..FF  FFFFF  FFFFF  F | 100 1576 1586 14 HTML blocks
    .....  ..F..  .....  F | 101 1590 1598 2 HTML blocks
    F..F.  FFFFF  FFFFF  F | 102 1602 1610 13 HTML blocks
    F..FF  FFFFF  FFFFF  F | 103 1614 1642 14 HTML blocks
    F..FF  ..F.F  FFFFF  . | 104 1646 1654 10 HTML blocks
    F..F.  ..F..  FFF.F  . | 105 1659 1669 7 HTML blocks
    F..FF  FFFFF  FFFFF  F | 106 1674 1684 14 HTML blocks
    F..FF  FFFFF  FFFFF  F | 107 1688 1694 14 HTML blocks
    F..FF  FFFFF  F.FFF  F | 108 1724 1734 13 HTML blocks
    .....  ..FF.  .F...  . | 109 1738 1746 3 HTML blocks
    .....  ..F..  .....  . | 110 1759 1779 1 HTML blocks
    .....  FF...  .....  . | 111 1806 1812 2 Link reference definitions
    ....F  FFFFF  ...F.  F | 112 1814 1822 8 Link reference definitions
    F..FF  FFFFF  .F.FF  F | 113 1824 1830 12 Link reference definitions
    F..FF  FFFFF  F.FFF  F | 114 1832 1840 13 Link reference definitions
    ....F  FF.FF  ...F.  . | 115 1844 1851 6 Link reference definitions
    F....  ....F  .F.F.  . | 116 1855 1862 4 Link reference definitions
    .....  FF...  .....  . | 117 1866 1872 2 Link reference definitions
    F..FF  FFFFF  FF.FF  F | 118 1877 1884 13 Link reference definitions
    .....  FF...  F....  . | 119 1889 1895 3 Link reference definitions
    F..FF  FFFFF  FFFFF  F | 120 1897 1903 14 Link reference definitions
    ....F  FFFFF  FFFF.  . | 121 1908 1911 10 Link reference definitions
    F...F  FFF.F  F..F.  F | 122 1916 1920 9 Link reference definitions
    ....F  FFF.F  .F.F.  F | 123 1925 1933 8 Link reference definitions
    F..FF  FFF.F  .FFFF  . | 124 1938 1948 11 Link reference definitions
    F..F.  FF.FF  ...FF  F | 125 1953 1962 9 Link reference definitions
    ....F  FF.FF  FFF..  F | 126 1967 1976 9 Link reference definitions
    .....  FF.F.  .....  . | 127 1981 1994 3 Link reference definitions
    F..F.  FFFFF  F.FFF  F | 128 2001 2009 12 Link reference definitions
    .....  .....  .....  . | 129 2023 2030 0 Paragraphs
    .....  .....  .....  . | 130 2034 2045 0 Paragraphs
    .....  .....  .....  . | 131 2049 2057 0 Paragraphs
    .....  .....  .....  . | 132 2061 2067 0 Paragraphs
    .....  .....  .....  . | 133 2072 2080 0 Paragraphs
    .....  .....  .....  . | 134 2085 2091 0 Paragraphs
    ....F  ..F.F  .F...  . | 135 2093 2100 4 Paragraphs
    ....F  FFF.F  ...F.  F | 136 2106 2112 7 Paragraphs
    ....F  ...FF  FF...  F | 137 2122 2134 6 Blank lines
    ....F  ...FF  FF...  F | 138 2190 2200 6 Block quotes
    ....F  ...FF  FF...  F | 139 2204 2214 6 Block quotes
    ....F  ..FFF  FFF..  F | 140 2218 2228 8 Block quotes
    .....  ..F.F  .F...  . | 141 2232 2241 3 Block quotes
    ....F  ...FF  FF...  F | 142 2246 2256 6 Block quotes
    .....  ....F  .....  . | 143 2261 2271 1 Block quotes
    F..FF  FFFF.  FFFFF  F | 144 2277 2285 13 Block quotes
    F..FF  FFFF.  FFFFF  F | 145 2287 2299 13 Block quotes
    F..FF  FFFFF  FFFFF  F | 146 2301 2311 14 Block quotes
    F..FF  FFFFF  FFFFF  F | 147 2313 2323 14 Block quotes
    .....  FF.F.  .....  F | 148 2327 2332 4 Block quotes
    .....  FF.F.  .....  F | 149 2334 2341 4 Block quotes
    .....  FF.F.  .....  F | 150 2345 2353 4 Block quotes
    F..F.  FFFF.  F.FFF  F | 151 2357 2368 11 Block quotes
    .....  .....  .....  . | 152 2378 2386 0 Block quotes
    .....  .....  .....  . | 153 2390 2399 0 Block quotes
    F...F  .....  .F...  . | 154 2403 2411 3 Block quotes
    F..FF  ...F.  FFFFF  . | 155 2416 2428 9 Block quotes
    .....  ....F  .....  . | 156 2433 2441 1 Block quotes
    .....  .....  .....  . | 157 2443 2452 0 Block quotes
    F..FF  FFFF.  FFFFF  F | 158 2454 2463 13 Block quotes
    .....  .F..F  .....  . | 159 2469 2481 2 Block quotes
    .....  .F..F  .....  . | 160 2483 2497 2 Block quotes
    F..F.  FFFFF  FFFFF  F | 161 2504 2516 13 Block quotes
    .....  ..F.F  .F...  . | 162 2548 2563 3 List items
    .....  ..F.F  .F...  . | 163 2569 2588 3 List items
    ...F.  FFFF.  .....  F | 164 2601 2610 6 List items
    F....  .....  FFF.F  . | 165 2612 2623 5 List items
    F..F.  FFFFF  FFFFF  F | 166 2625 2635 13 List items
    .....  .....  .....  . | 167 2637 2648 0 List items
    .....  .FF.F  .FF..  . | 168 2658 2673 5 List items
    .....  .FF.F  ..F..  . | 169 2684 2697 4 List items
    F..FF  FFFFF  FFFFF  F | 170 2703 2739 14 List items
    ...FF  FFF.F  .FF.F  F | 171 2743 2765 10 List items
    F..F.  FFF.F  FFF.F  F | 172 2783 2795 11 List items
    F..FF  FFFFF  FFFFF  F | 173 2799 2811 14 List items
    .....  ..F.F  .F...  . | 174 2817 2829 3 List items
    F..FF  FFFFF  FFFFF  F | 175 2831 2847 14 List items
    F..FF  FFFFF  FFFFF  F | 176 2852 2868 14 List items
    .....  .....  .....  . | 177 2877 2884 0 List items
    ...F.  FFFF.  .....  F | 178 2886 2895 6 List items
    F....  .....  FFF.F  . | 179 2902 2913 5 List items
    F..F.  FFF.F  FFFFF  F | 180 2924 2943 12 List items
    F..F.  FFF.F  FFFFF  F | 181 2947 2966 12 List items
    F..F.  FFF.F  FFFFF  F | 182 2970 2989 12 List items
    .....  ..F.F  .F...  . | 183 2993 3008 3 List items
    F..F.  FFF.F  FFFFF  F | 184 3023 3042 12 List items
    .....  ....F  .F...  . | 185 3046 3054 2 List items
    F..F.  FFF.F  .F..F  F | 186 3058 3072 9 List items
    F..F.  FFF.F  .F..F  F | 187 3074 3088 9 List items
    F..F.  FF...  FFF.F  F | 188 3100 3116 9 List items
    F..F.  FFFF.  ....F  F | 189 3120 3130 8 List items
    F..FF  FFFFF  FFFFF  F | 190 3134 3145 14 List items
    F..FF  FFFFF  FFFFF  F | 191 3149 3159 14 List items
    F..F.  F.F..  ....F  . | 192 3163 3173 5 List items
    F..FF  FFFFF  FFFFF  F | 193 3175 3189 14 List items
    F..FF  FFFFF  F.FFF  F | 194 3193 3203 13 List items
    F..FF  FFFFF  F.FFF  F | 195 3205 3211 13 List items
    F.FFF  FFFFF  FFFFF  F | 196 3215 3229 15 List items
    F..FF  FFFFF  FFFFF  F | 197 3451 3463 14 Lists
    F..FF  FFFFF  FFFFF  F | 198 3465 3477 14 Lists
    F..FF  FFF..  FFFFF  F | 199 3483 3493 12 Lists
    F..FF  FFFFF  FFFFF  F | 200 3498 3506 14 Lists
    F..FF  FFF.F  FFFFF  F | 201 3563 3582 13 Lists
    F..FF  FFF.F  FFFFF  F | 202 3588 3602 13 Lists
    F..FF  FFF.F  FFFFF  F | 203 3606 3627 13 Lists
    F..FF  FFF.F  FFFFF  F | 204 3634 3650 13 Lists
    F..FF  FFF.F  FFFFF  F | 205 3652 3673 13 Lists
    F..F.  FFFF.  ....F  F | 206 3680 3698 8 Lists
    F..FF  FFFF.  .F.FF  F | 207 3703 3720 11 Lists
    F..FF  FFFFF  .FFFF  F | 208 3724 3739 13 Lists
    F..FF  FFFF.  FFFFF  F | 209 3745 3764 13 Lists
    F..FF  FFFF.  FFFFF  F | 210 3766 3784 13 Lists
    F..FF  FFFFF  FFF.F  F | 211 3788 3807 13 Lists
    F..F.  FFFFF  FFF.F  F | 212 3813 3831 12 Lists
    F..FF  FFF..  FFF.F  F | 213 3836 3850 11 Lists
    F..FF  FFFFF  FFFFF  F | 214 3855 3873 14 Lists
    .....  .....  .....  . | 215 3877 3883 0 Lists
    .....  .....  FFF..  . | 216 3885 3896 3 Lists
    F...F  FFF..  FFFFF  . | 217 3900 3915 10 Lists
    ....F  ..F..  FFF..  . | 218 3917 3942 5 Lists
    .....  .....  .....  . | 219 3950 3954 0 Inlines
    F..FF  FFFFF  F.FFF  F | 220 3963 3967 13 Backslash escapes
    .....  .....  .F...  . | 221 3972 3976 1 Backslash escapes
    F...F  FFFFF  F..F.  F | 222 3981 3999 10 Backslash escapes
    .....  .....  .....  . | 223 4003 4007 0 Backslash escapes
    F..FF  FFFFF  F.FFF  F | 224 4012 4018 13 Backslash escapes
    .....  ..FF.  .....  . | 225 4023 4027 2 Backslash escapes
    .....  ..F.F  .F...  . | 226 4029 4034 3 Backslash escapes
    ...F.  FFF.F  FFF.F  F | 227 4036 4043 10 Backslash escapes
    F..FF  FFFFF  FFFFF  F | 228 4045 4049 14 Backslash escapes
    ....F  ..F.F  .....  . | 229 4051 4055 3 Backslash escapes
    F..FF  ..FFF  F.F.F  . | 230 4061 4065 9 Backslash escapes
    F..FF  FFFFF  F.F.F  F | 231 4067 4073 12 Backslash escapes
    F..FF  FFFFF  FFFFF  F | 232 4075 4082 14 Backslash escapes
    F..FF  FFFFF  F.FFF  F | 233 4107 4111 13 Entities
    F..FF  FFFFF  FFFFF  F | 234 4119 4123 14 Entities
    F..FF  FFFFF  FFFFF  F | 235 4129 4133 14 Entities
    F..F.  FF.FF  F.FFF  F | 236 4137 4141 11 Entities
    .....  .....  .....  . | 237 4147 4151 0 Entities
    F..F.  FF.FF  F.FFF  F | 238 4156 4160 11 Entities
    ....F  ..F.F  .....  . | 239 4166 4170 3 Entities
    F..FF  FFFFF  FFFFF  F | 240 4172 4176 14 Entities
    F..FF  FFFFF  FFFFF  F | 241 4178 4184 14 Entities
    F..FF  FFFFF  FFFFF  F | 242 4186 4193 14 Entities
    .....  .....  .....  . | 243 4197 4201 0 Entities
    .....  ..F.F  .F...  . | 244 4203 4208 3 Entities
    .....  .....  .....  . | 245 4224 4228 0 Code span
    ....F  ..F.F  ...F.  . | 246 4233 4237 4 Code span
    F..FF  ..FFF  ....F  . | 247 4242 4246 7 Code span
    F..FF  FFF.F  F.FFF  F | 248 4250 4256 12 Code span
    .....  .....  .....  . | 249 4261 4266 0 Code span
    F..FF  ..F.F  ....F  . | 250 4281 4285 6 Code span
    .....  .....  .....  . | 251 4290 4294 0 Code span
    ...F.  ...FF  ....F  . | 252 4305 4309 4 Code span
    F....  ...FF  ...FF  . | 253 4313 4317 5 Code span
    F...F  FFFFF  FFFF.  F | 254 4321 4325 12 Code span
    ....F  FFF.F  .....  F | 255 4329 4333 6 Code span
    F..F.  FFFFF  FFFFF  F | 256 4338 4342 13 Code span
    .....  .....  .....  . | 257 4344 4348 0 Code span
    .....  .....  .....  . | 258 4483 4487 0 Emphasis and strong emphasis
    .....  ..FF.  .....  . | 259 4492 4496 2 Emphasis and strong emphasis
    FF.FF  FFFFF  FFFFF  . | 260 4500 4504 14 Emphasis and strong emphasis
    .....  .....  .....  . | 261 4508 4512 0 Emphasis and strong emphasis
    F....  .....  .....  . | 262 4514 4518 1 Emphasis and strong emphasis
    .....  .....  .....  . | 263 4522 4526 0 Emphasis and strong emphasis
    .....  ..FF.  .....  . | 264 4531 4535 2 Emphasis and strong emphasis
    F..F.  FFFF.  ....F  F | 265 4539 4543 8 Emphasis and strong emphasis
    ...F.  FFF..  ....F  F | 266 4545 4549 6 Emphasis and strong emphasis
    ....F  ....F  FFF..  . | 267 4553 4557 5 Emphasis and strong emphasis
    .....  ..FFF  FFF..  . | 268 4564 4568 6 Emphasis and strong emphasis
    F....  .....  .....  . | 269 4572 4576 1 Emphasis and strong emphasis
    .....  ..FFF  FFF..  . | 270 4584 4588 6 Emphasis and strong emphasis
    ...F.  FFF.F  ....F  F | 271 4592 4596 7 Emphasis and strong emphasis
    F...F  .....  FFF..  . | 272 4598 4602 5 Emphasis and strong emphasis
    ...F.  FFF.F  ....F  F | 273 4604 4608 7 Emphasis and strong emphasis
    .....  .....  .....  . | 274 4612 4616 0 Emphasis and strong emphasis
    .....  FFFF.  ...F.  F | 275 4621 4625 6 Emphasis and strong emphasis
    .....  .....  .....  . | 276 4629 4633 0 Emphasis and strong emphasis
    .....  .....  .....  . | 277 4637 4641 0 Emphasis and strong emphasis
    .....  FFFF.  ...F.  F | 278 4646 4650 6 Emphasis and strong emphasis
    F..F.  FFFF.  ...FF  F | 279 4654 4658 9 Emphasis and strong emphasis
    F..F.  FFFF.  ...FF  F | 280 4660 4664 9 Emphasis and strong emphasis
    ....F  ....F  FFF..  . | 281 4666 4670 5 Emphasis and strong emphasis
    F..FF  FFFFF  F.FFF  F | 282 4672 4676 13 Emphasis and strong emphasis
    .....  FFFFF  FFFFF  F | 283 4683 4687 11 Emphasis and strong emphasis
    .....  .....  .....  . | 284 4694 4698 0 Emphasis and strong emphasis
    .....  FFFFF  FFFFF  F | 285 4705 4709 11 Emphasis and strong emphasis
    F..F.  FFFFF  ...FF  F | 286 4713 4717 10 Emphasis and strong emphasis
    ....F  .....  FFF..  . | 287 4719 4723 4 Emphasis and strong emphasis
    F..F.  FFFFF  .F.FF  F | 288 4725 4729 11 Emphasis and strong emphasis
    .....  .....  .....  . | 289 4736 4740 0 Emphasis and strong emphasis
    .....  .....  .....  . | 290 4742 4748 0 Emphasis and strong emphasis
    ...F.  .....  ....F  . | 291 4753 4757 2 Emphasis and strong emphasis
    F..FF  FFFFF  F.FFF  F | 292 4759 4763 13 Emphasis and strong emphasis
    F..FF  FFFFF  FFF.F  F | 293 4765 4769 13 Emphasis and strong emphasis
    F..FF  FFFFF  FFFFF  F | 294 4771 4775 14 Emphasis and strong emphasis
    ...F.  .....  ....F  . | 295 4777 4781 2 Emphasis and strong emphasis
    F...F  FFFFF  FFFF.  F | 296 4785 4789 12 Emphasis and strong emphasis
    ...F.  FFFFF  ....F  F | 297 4795 4799 8 Emphasis and strong emphasis
    ...F.  FF...  ....F  F | 298 4801 4805 5 Emphasis and strong emphasis
    F...F  FFFFF  FFFF.  F | 299 4811 4815 12 Emphasis and strong emphasis
    F..FF  FFFF.  ...FF  F | 300 4820 4824 10 Emphasis and strong emphasis
    F...F  FFFF.  .....  F | 301 4826 4830 7 Emphasis and strong emphasis
    .....  .....  .....  . | 302 4834 4838 0 Emphasis and strong emphasis
    ....F  FFFF.  .....  F | 303 4840 4844 6 Emphasis and strong emphasis
    .....  .....  .....  . | 304 4852 4856 0 Emphasis and strong emphasis
    .....  .....  .....  . | 305 4858 4864 0 Emphasis and strong emphasis
    .....  .....  .....  . | 306 4869 4873 0 Emphasis and strong emphasis
    F..FF  FFFFF  F.FFF  F | 307 4875 4879 13 Emphasis and strong emphasis
    F..FF  FFFFF  FFF.F  F | 308 4881 4885 13 Emphasis and strong emphasis
    F..FF  FFFFF  FFFFF  F | 309 4887 4891 14 Emphasis and strong emphasis
    .....  .....  .....  . | 310 4893 4897 0 Emphasis and strong emphasis
    F..FF  FFFFF  FFFFF  F | 311 4901 4905 14 Emphasis and strong emphasis
    ...F.  ....F  .....  . | 312 4911 4915 2 Emphasis and strong emphasis
    F..F.  ..F..  ....F  . | 313 4917 4921 4 Emphasis and strong emphasis
    F..FF  FFFF.  ...FF  F | 314 4925 4931 10 Emphasis and strong emphasis
    .....  .....  .....  . | 315 4933 4937 0 Emphasis and strong emphasis
    .....  .....  .....  . | 316 4941 4945 0 Emphasis and strong emphasis
    ....F  FFFF.  .....  F | 317 4947 4951 6 Emphasis and strong emphasis
    .....  FF.F.  F....  F | 318 4956 4960 5 Emphasis and strong emphasis
    F....  .....  .....  . | 319 4962 4966 1 Emphasis and strong emphasis
    .....  ....F  .F...  . | 320 4968 4972 2 Emphasis and strong emphasis
    .....  FFFF.  .....  F | 321 4974 4978 5 Emphasis and strong emphasis
    F....  .....  .....  . | 322 4980 4984 1 Emphasis and strong emphasis
    .....  ....F  .F...  . | 323 4986 4990 2 Emphasis and strong emphasis
    ....F  FFFFF  .F.F.  F | 324 4996 5000 9 Emphasis and strong emphasis
    F...F  ..FFF  .F.F.  . | 325 5002 5006 7 Emphasis and strong emphasis
    ....F  FFFFF  ...FF  F | 326 5008 5012 9 Emphasis and strong emphasis
    ....F  FFFFF  FFFF.  F | 327 5014 5018 11 Emphasis and strong emphasis
    .....  FF.F.  .....  F | 328 5020 5024 4 Emphasis and strong emphasis
    F....  FFFF.  F....  F | 329 5026 5030 7 Emphasis and strong emphasis
    .....  FF.F.  F....  F | 330 5035 5039 5 Emphasis and strong emphasis
    F....  .....  .....  . | 331 5041 5045 1 Emphasis and strong emphasis
    .....  ....F  .F...  . | 332 5047 5051 2 Emphasis and strong emphasis
    .....  FFFF.  .....  F | 333 5053 5057 5 Emphasis and strong emphasis
    F....  .....  .....  . | 334 5059 5063 1 Emphasis and strong emphasis
    .....  ....F  .F...  . | 335 5065 5069 2 Emphasis and strong emphasis
    ....F  FFFFF  .F.F.  F | 336 5071 5075 9 Emphasis and strong emphasis
    F...F  ..FFF  .F.F.  . | 337 5081 5085 7 Emphasis and strong emphasis
    ....F  FFFFF  ...FF  F | 338 5087 5091 9 Emphasis and strong emphasis
    ....F  FFFFF  FFFF.  F | 339 5093 5097 11 Emphasis and strong emphasis
    .....  FF.F.  .....  F | 340 5099 5103 4 Emphasis and strong emphasis
    F....  FFFF.  F....  F | 341 5105 5109 7 Emphasis and strong emphasis
    .....  .....  .....  . | 342 5114 5118 0 Emphasis and strong emphasis
    ....F  FFF..  .....  F | 343 5120 5124 5 Emphasis and strong emphasis
    .....  .....  .....  . | 344 5126 5130 0 Emphasis and strong emphasis
    ....F  FFF..  .....  F | 345 5132 5136 5 Emphasis and strong emphasis
    F..FF  FFF.F  FFF.F  F | 346 5141 5145 12 Emphasis and strong emphasis
    F..FF  FFF.F  FFF.F  F | 347 5147 5151 12 Emphasis and strong emphasis
    F..FF  FFFFF  FFF.F  F | 348 5157 5161 13 Emphasis and strong emphasis
    .....  ..F..  .....  . | 349 5165 5169 1 Emphasis and strong emphasis
    F..FF  FFFFF  FFF.F  F | 350 5171 5175 13 Emphasis and strong emphasis
    .....  ..F.F  FFF..  . | 351 5179 5183 5 Emphasis and strong emphasis
    F..FF  FFFFF  FFFFF  F | 352 5185 5189 14 Emphasis and strong emphasis
    F...F  FFFFF  FFFFF  F | 353 5194 5198 13 Emphasis and strong emphasis
    F...F  FFFFF  FFFFF  F | 354 5200 5204 13 Emphasis and strong emphasis
    F....  FF.FF  ....F  F | 355 5208 5212 7 Emphasis and strong emphasis
    F....  FF.FF  .....  F | 356 5214 5218 6 Emphasis and strong emphasis
    F..F.  ..FFF  ....F  . | 357 5220 5224 6 Emphasis and strong emphasis
    F..FF  ..FFF  ....F  . | 358 5226 5230 7 Emphasis and strong emphasis
    F..FF  ..FFF  ....F  . | 359 5232 5236 7 Emphasis and strong emphasis
    .....  ...F.  ....F  . | 360 5238 5242 2 Emphasis and strong emphasis
    .....  ...F.  ....F  . | 361 5244 5248 2 Emphasis and strong emphasis
    F..F.  ...FF  .F..F  . | 362 5250 5254 6 Emphasis and strong emphasis
    F..F.  ...FF  .F..F  . | 363 5256 5260 6 Emphasis and strong emphasis
    .....  .....  .....  . | 364 5335 5339 0 Links
    .....  .....  .....  . | 365 5343 5347 0 Links
    F....  .....  .....  . | 366 5351 5355 1 Links
    F....  .....  .....  F | 367 5357 5361 2 Links
    F..FF  FFFFF  .F.FF  F | 368 5366 5370 12 Links
    F...F  FFFFF  F.F..  F | 369 5372 5376 10 Links
    F..FF  FFFFF  .F.FF  . | 370 5380 5386 11 Links
    F....  .F.FF  ...F.  F | 371 5390 5394 6 Links
    F..FF  FFFFF  FFFFF  F | 372 5399 5403 14 Links
    F...F  .F.FF  F.FF.  . | 373 5405 5409 8 Links
    F....  .F.FF  .....  F | 374 5411 5415 5 Links
    ....F  FFFFF  F.F..  F | 375 5420 5424 9 Links
    F..FF  FFFFF  FFFFF  F | 376 5431 5435 14 Links
    F...F  FFFFF  FFFF.  F | 377 5441 5445 12 Links
    F..FF  FFFFF  FFFFF  F | 378 5449 5457 14 Links
    F..FF  FFFFF  F.FFF  F | 379 5461 5465 13 Links
    F..FF  FFFFF  FFFFF  F | 380 5469 5473 14 Links
    .....  ....F  .....  . | 381 5477 5481 1 Links
    .....  FFF.F  .....  F | 382 5499 5504 5 Links
    F..F.  ..F.F  F...F  . | 383 5509 5513 6 Links
    ...F.  ..F.F  .....  F | 384 5518 5522 4 Links
    .....  ...F.  .....  . | 385 5524 5528 1 Links
    .....  ....F  .....  . | 386 5530 5534 1 Links
    .....  ...F.  .F...  . | 387 5536 5540 2 Links
    ...F.  .....  ....F  . | 388 5544 5548 2 Links
    F....  .F...  .....  F | 389 5550 5554 3 Links
    F..FF  FFFFF  FFFFF  F | 390 5558 5562 14 Links
    F..FF  FFFFF  FFFFF  F | 391 5564 5568 14 Links
    F....  FF.FF  ....F  F | 392 5573 5577 7 Links
    ....F  ..F.F  F.F..  . | 393 5579 5583 5 Links
    F..FF  FFFFF  .F.FF  F | 394 5588 5592 12 Links
    F..F.  ...FF  ...FF  . | 395 5594 5598 6 Links
    F..FF  FFFFF  FFFFF  F | 396 5600 5604 14 Links
    .....  .....  .....  . | 397 5635 5641 0 Links
    ...F.  ..F.F  .....  F | 398 5649 5655 4 Links
    .....  ...F.  .F...  . | 399 5657 5663 2 Links
    ...F.  .....  ....F  . | 400 5667 5673 2 Links
    F....  .F...  .....  F | 401 5675 5681 3 Links
    F..FF  FFFFF  FFFFF  F | 402 5685 5691 14 Links
    F..FF  FFFFF  FFFFF  F | 403 5693 5699 14 Links
    F....  FF.FF  ....F  F | 404 5708 5714 7 Links
    .....  ....F  .....  . | 405 5716 5722 1 Links
    F..FF  FFFFF  .F.FF  F | 406 5727 5733 12 Links
    F..F.  ...FF  ...FF  . | 407 5735 5741 6 Links
    F..FF  FFFFF  FFFFF  F | 408 5743 5749 14 Links
    .....  .....  .....  . | 409 5753 5759 0 Links
    ...FF  .F..F  F.FFF  . | 410 5763 5769 8 Links
    F..FF  FFFFF  ..FFF  F | 411 5774 5781 12 Links
    .....  .....  .....  . | 412 5786 5792 0 Links
    .....  ....F  .....  . | 413 5794 5801 1 Links
    F..FF  FFFFF  FF.FF  F | 414 5806 5814 13 Links
    ....F  ..F.F  F.F..  . | 415 5820 5826 5 Links
    F..FF  FFFFF  ....F  F | 416 5831 5838 10 Links
    .....  FFF.F  FFF..  F | 417 5840 5847 8 Links
    .....  FFF..  .FF..  F | 418 5849 5856 6 Links
    .....  FF..F  .F.F.  F | 419 5858 5864 6 Links
    .....  .....  .....  . | 420 5875 5881 0 Links
    .....  ..F.F  .....  . | 421 5883 5889 2 Links
    .....  .....  .....  . | 422 5893 5899 0 Links
    .....  ....F  .....  . | 423 5905 5912 1 Links
    .....  FF...  .....  . | 424 5924 5930 2 Links
    .....  FFF.F  .....  . | 425 5932 5938 4 Links
    .....  FFF.F  .....  . | 426 5940 5946 4 Links
    .....  FF...  .....  . | 427 5950 5956 2 Links
    ..F..  FF...  .....  . | 428 5960 5966 3 Links
    .....  .....  .....  . | 429 5971 5977 0 Links
    F..F.  FFFFF  ....F  F | 430 5982 5988 9 Links
    F..F.  ...FF  ...FF  . | 431 5992 5998 6 Links
    .....  .....  .....  . | 432 6002 6009 0 Links
    .....  FFF.F  FFF..  F | 433 6014 6020 8 Links
    .....  FF...  .....  . | 434 6025 6032 2 Links
    .....  FFF.F  FFF..  F | 435 6037 6044 8 Links
    .....  .....  FF...  . | 436 6059 6063 2 Images
    F..FF  FFFFF  FFFFF  F | 437 6065 6071 14 Images
    F..FF  FFFF.  FFFFF  F | 438 6073 6077 13 Images
    F..FF  FFFF.  FFFFF  F | 439 6079 6083 13 Images
    F..FF  FFFFF  FFFFF  F | 440 6092 6098 14 Images
    F..FF  FFFF.  FFFFF  F | 441 6100 6106 13 Images
    .....  .F...  FF...  F | 442 6108 6112 4 Images
    .....  F....  .....  . | 443 6114 6118 1 Images
    .....  .F...  FF...  F | 444 6120 6124 4 Images
    .....  .F...  FF...  F | 445 6126 6130 4 Images
    .....  .....  FF...  F | 446 6134 6140 3 Images
    .....  .....  FF...  F | 447 6142 6148 3 Images
    .....  ..F..  FF...  . | 448 6152 6158 3 Images
    F..FF  FFFFF  FFFFF  F | 449 6160 6166 14 Images
    .....  ..F..  FF...  . | 450 6170 6176 3 Images
    .....  ..F.F  FF...  . | 451 6181 6188 4 Images
    .....  FFF..  FF...  F | 452 6192 6198 6 Images
    F..FF  FFFFF  FFFFF  F | 453 6200 6206 14 Images
    F...F  FFF.F  FFFF.  F | 454 6210 6217 11 Images
    .....  FFF..  FF...  F | 455 6221 6227 6 Images
    .....  .....  .....  . | 456 6232 6238 0 Images
    F....  FF...  ....F  . | 457 6243 6249 4 Images
    .....  .....  .F...  . | 458 6296 6300 1 Autolinks
    .....  ....F  .F...  . | 459 6302 6306 2 Autolinks
    ....F  FFF..  .F.F.  F | 460 6308 6312 7 Autolinks
    ....F  FFFFF  FFFF.  F | 461 6316 6320 11 Autolinks
    F..FF  FFFFF  FFFFF  F | 462 6324 6328 14 Autolinks
    .....  .....  .F...  . | 463 6345 6349 1 Autolinks
    ....F  FF.FF  .F...  F | 464 6351 6355 7 Autolinks
    .....  .F...  ...F.  F | 465 6359 6363 3 Autolinks
    F..F.  FF.FF  FFFFF  F | 466 6365 6369 12 Autolinks
    F....  .F.FF  ...F.  F | 467 6371 6375 6 Autolinks
    F..FF  FF.FF  .F.FF  F | 468 6377 6381 11 Autolinks
    F..F.  FF.FF  .F.FF  F | 469 6383 6387 10 Autolinks
    F....  ...F.  .....  . | 470 6389 6393 2 Autolinks
    .....  .....  .....  . | 471 6395 6399 0 Autolinks
    ....F  ..F.F  .....  . | 472 6479 6483 3 Raw HTML
    ....F  ..F..  .....  . | 473 6487 6491 2 Raw HTML
    ....F  F.F.F  .....  . | 474 6495 6501 4 Raw HTML
    F..FF  ..F.F  FFF.F  . | 475 6505 6511 9 Raw HTML
    F..FF  FF.FF  F.FFF  F | 476 6515 6519 12 Raw HTML
    F..FF  FF.FF  FF.FF  F | 477 6523 6527 12 Raw HTML
    F..FF  FF..F  FFFFF  F | 478 6531 6535 12 Raw HTML
    F..F.  FF.FF  FFFFF  F | 479 6539 6545 12 Raw HTML
    F..FF  FF.FF  FFFFF  F | 480 6549 6553 13 Raw HTML
    ....F  F.F.F  .....  . | 481 6557 6563 4 Raw HTML
    F..FF  FF.FF  FFFFF  F | 482 6567 6571 13 Raw HTML
    F..F.  ..F..  ....F  . | 483 6575 6581 4 Raw HTML
    F...F  FF.FF  FFFF.  F | 484 6583 6587 11 Raw HTML
    F..F.  ..FFF  F.FFF  . | 485 6591 6595 9 Raw HTML
    F..FF  ..FFF  F.FFF  . | 486 6599 6603 10 Raw HTML
    F..FF  FFFFF  FFFFF  F | 487 6607 6611 14 Raw HTML
    ....F  ..F.F  .....  . | 488 6615 6619 3 Raw HTML
    ....F  ..F.F  .....  . | 489 6623 6627 3 Raw HTML
    F..FF  FFFFF  FFFFF  F | 490 6629 6633 14 Raw HTML
    .....  FF...  .....  F | 491 6642 6648 3 Hard line breaks
    F..FF  FFFFF  F.FFF  F | 492 6653 6659 13 Hard line breaks
    ....F  FFF.F  ...F.  F | 493 6663 6669 7 Hard line breaks
    F..FF  FFFFF  FFFFF  F | 494 6673 6679 14 Hard line breaks
    F..FF  FFFFF  FFFFF  F | 495 6681 6687 14 Hard line breaks
    .....  FF...  .....  F | 496 6692 6698 3 Hard line breaks
    F..FF  FFFFF  F.FFF  F | 497 6700 6706 13 Hard line breaks
    .....  .F...  .....  F | 498 6710 6715 2 Hard line breaks
    .....  .....  .....  . | 499 6717 6722 0 Hard line breaks
    ....F  FFF.F  ...F.  F | 500 6726 6732 7 Hard line breaks
    ....F  ..F.F  .....  . | 501 6734 6740 3 Hard line breaks
    F....  .....  FF...  . | 502 6746 6750 3 Hard line breaks
    .....  .....  .....  . | 503 6752 6756 0 Hard line breaks
    F...F  F..FF  FF...  F | 504 6758 6762 8 Hard line breaks
    ....F  ...FF  FF...  F | 505 6764 6768 6 Hard line breaks
    .....  .....  .....  . | 506 6779 6785 0 Soft line breaks
    .....  .....  .....  . | 507 6790 6796 0 Soft line breaks
    F...F  ....F  F....  . | 508 6809 6813 4 Textual content
    .....  .....  .....  . | 509 6815 6819 0 Textual content
    .....  .....  .....  . | 510 6823 6827 0 Textual content

    Compiler id | Total time | Total errors | Error percent

    blackfriday     1.9856s  235  46%
    cmark           1.8851s    1   0%
    commonmarkjs   36.8647s    2   0%
    hoedown         1.7733s  221  43%
    kramdown       86.0154s  247  48%
    markdown2      27.0338s  278  54%
    markdown_pl    14.2149s  287  56%
    markdownjs     37.3201s  302  59%
    marked         32.7017s  258  50%
    maruku         79.1347s  316  61%
    multimarkdown   1.9084s  239  46%
    pandoc          5.9902s  268  52%
    peg_markdown    2.6106s  211  41%
    rdiscount      38.7256s  200  39%
    redcarpet      39.8762s  229  44%
    showdown       41.9013s  285  55%
