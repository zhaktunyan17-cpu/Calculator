[app]

# Հավելվածի անունը և փաթեթի տվյալները
title = Calculator
package.name = calculator
package.domain = org.test

# Հիմնական ֆայլի տեղը
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Հավելվածի տարբերակը
version = 0.1

# Պահանջվող գրադարանները
requirements = python3,kivy

# Էկրանի ուղղվածությունը
orientation = portrait

# Ամբողջ էկրանով (0 = ոչ, 1 = այո)
fullscreen = 0

# Միայն ժամանակակից 64-բիթանոց հեռախոսների համար (արագ հավաքման համար)
android.archs = arm64-v8a

# Թույլատրել պահուստավորումը
android.allow_backup = True

[buildozer]

# Լոգերի մակարդակը (2 = մանրամասն)
log_level = 2

# Զգուշացում root-ի մասին (0 = անջատված)
warn_on_root = 0
