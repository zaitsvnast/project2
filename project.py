# данная программа предлагает пользователю определить его тип мышления.
# для этого пользователю предлагается ответить на вопросы.
# ответом могут служить слова "да" или "нет".
# если ответ "да", то пользователь вводит "1".
# если ответ "нет", то "0".


# букве "p" соответствует предметно-действенный тип мышления.
# букве "a" соответствует абстрактно-символический тип мышления.
# букве "s" соответствует словесно-логический тип мышления.
# букве "o" соответствует наглядно-образный тип мышления.
# букве "k" соответствует креативный тип мышления.


p1 = int(input('1. Мне легче что-либо сделать самому, чем объяснить другому: '))
a1 = int(input('2. Мне интересно составлять компьютерные программы: '))
s1 = int(input('3. Я люблю читать книги: '))
o1 = int(input('4. Мне нравится живопись, скульптура, архитектура: '))
k1 = int(input('5. Даже в отлаженном деле я стараюсь что-то улучшить: '))
p2 = int(input('6. Я лучше понимаю, если мне объясняют на предметах или рисунках: '))
a2 = int(input('7. Я люблю играть в шахматы: '))
s2 = int(input('8. Я легко излагаю свои мысли как в устной, так и в письменной форме: '))
o2 = int(input('9. Когда я читаю книгу, я чётко вижу её героев и описываемые события: '))
k2 = int(input('10. Я предпочитаю самостоятельно планировать свою работу: '))
p3 = int(input('11. Мне нравится всё делать своими руками: '))
a3 = int(input('12. В детстве я создавал(а) свой шифр для переписки с сдрузьями: '))
s3 = int(input('13. Я придаю большое значение сказанному слову: '))
o3 = int(input('14. Знакомые мелодии вызывают у меня в голове определённые картины: '))
k3 = int(input('15. Разнообразные увлечения делают жизнь человека богаче и ярче: '))
p4 = int(input('16. При решении задач мне легче идти методом проб и ошибок: '))
a4 = int(input('17. Мне интересно разбираться в природе физических явлений:'))
s4 = int(input('18. Мне интересна работа ведущего теле-радиопрограмм, журналиста: '))
o4 = int(input('19. Мне легко представить предмет или животное, которых нет в природе:'))
k4 = int(input('20. Мне больше нравится сам процесс деятельности, чем сам результат: '))
p5 = int(input('21. Мне нравилось в детстве собирать конструктор из деталей, лего: '))
a5 = int(input('22. Я предпочитаю точные науки (математику, физику): '))
s5 = int(input('23. Меня восхищает точность и глубина некоторых стихов: '))
o5 = int(input('24. Знакомый запах вызывает у меня в голове прошлые события: '))
k5 = int(input('25. Я не хотел(а) бы подчинять свою жизнь определённой системе: '))
p6 = int(input('26. Когда я слышу музыку, мне хочется танцевать: '))
a6 = int(input('27. Я понимаю красоту математических формул: '))
s6 = int(input('28. Мне легко говорить перед любой аудиторией: '))
o6 = int(input('29. Я люблю посещать выставки, спектакли, концерты: '))
k6 = int(input('30. Я сомневаюсь даже в том, что для других очевидно: '))
p7 = int(input('31. Я люблю заниматься рукоделием, что-то мастерить: '))
a7 = int(input('32. Мне интересно было бы расшифровать древние тексты: '))
s7 = int(input('33. Я легко усваиваю грамматические конструкции языка: '))
o7 = int(input('34. Красота для меня важнее, чем польза: '))
k7 = int(input('35. Не люблю ходить одним и тем же путём: '))
p8 = int(input('36. Истинно только то, что можно потрогать руками: '))
a8 = int(input('37. Я легко запоминаю символы, формулы, условные обозначения: '))
s8 = int(input('38. Друзья любят слушать, когда я им что-то рассказываю: '))
o8 = int(input('39. Я легко могу представить в образах содержание рассказа или фильма: '))
k8 = int(input('40. Я не могу успокоиться, пока не доведу свою работу до совершенства: '))

p = p1+p2+p3+p4+p5+p6+p7+p8   # считаем общее количество баллов для каждого типа.
a = a1+a2+a3+a4+a5+a6+a7+a8
s = s1+s2+s3+s4+s5+s6+s7+s8
o = o1+o2+o3+o4+o5+o6+o7+o8
k = k1+k2+k3+k4+k5+k6+k7+k8

if p>a and p>s and p>o and p>k:                                  # программа выводит тот тип мышления,
    print('Результат: Предметно-действенный тип мышления')       # которому соответствует большее количество
elif a>p and a>s and a>o and a>k:                                # набранных баллов.
    print('Результат: Абстрактно-символический тип мышления')
elif s>p and s>a and s>o and s>k:
    print('Результат: Словесно-логический тип мышления')
elif o>p and o>a and o>s and o>k:
    print('Результат: Наглядно-образный тип мышления')
else:
    print('Результат: Креативное мышление')
