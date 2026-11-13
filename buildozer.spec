[app]

# Հավելվածի անունը, որը կերևա հեռախոսի էկրանին
title = Calculator

# Փաթեթի անունը (միայն փոքրատառերով, առանց բացատների)
package.name = calculator

# Փաթեթի դոմենը
package.domain = org.test

# Որտեղ է գտնվում main.py-ը (կետը նշանակում է ընթացիկ պանակը)
source.dir = .

# Ինչ ֆայլեր ներառել հավելվածի մեջ
source.include_exts = py,png,jpg,kv,atlas

# Հավելվածի տարբերակը
version = 0.1

# Անհրաժեշտ գրադարանները
requirements = python3,kivy

# Էկրանի դիրքը (portrait - ուղղահայաց, landscape - հորիզոնական)
orientation = portrait

# Ամբողջ էկրանով բացվելու ռեժիմ (0 = ոչ, 1 = այո)
fullscreen = 0

# Android-ի կարգավորումներ
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]

# Լոգերի մակարդակը (2-ը ցույց է տալիս մանրամասն ինֆորմացիա)
log_level = 2
warn_on_root = 1