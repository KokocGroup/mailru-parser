# -*- coding:utf-8 -*-
import unittest
from mailru_parser.tests import MailRuParserTests
from mailru_parser.mailru import MailRuParser


class MailRuParserTestCase(MailRuParserTests):
    def test1(self):
        html = self.get_data('not_found.html')
        serp = MailRuParser(html).get_serp()
        self.assertEqual(serp['sn'], [])
        self.assertEqual(serp['pc'], 0)

    def test2(self):
        html = self.get_data('not_found_1.html')
        serp = MailRuParser(html).get_serp()
        self.assertEqual(serp['sn'], [])
        self.assertEqual(serp['pc'], 0)

    def test3(self):
        html = self.get_data('2021-02-04.html')
        serp = MailRuParser(html).get_serp()

        self.assertEqual(serp['pc'], 24316859)
        self.assertEqual(len(serp['sn']), 10)

        self.assertEqual(serp['sn'][0]['d'], 'eapteka.ru')
        self.assertEqual(serp['sn'][0]['p'], 1)
        self.assertEqual(serp['sn'][0]['t'], u'<b>купить</b> блефарогель <b>1</b>')
        self.assertEqual(serp['sn'][0]['u'], 'http://eapteka.ru/goods/beauty/kosmetika_po_ukhodu_za_kozhey/kosmetika_dlya_glaz/blefarogel_1_geltek')
        self.assertEqual(serp['sn'][0]['s'], u'<b>Купить</b> Блефарогель <b>1</b> в интернет-аптеке в Москве, низкие цены и официальная инструкция по применению, честные отзывы покупателей и фармацевтов о Блефарогель <b>1</b>. Только сертифицированные медикаменты...')

        self.assertEqual(serp['sn'][9]['d'], 'alex-argo.ru')
        self.assertEqual(serp['sn'][9]['p'], 10)
        self.assertEqual(serp['sn'][9]['t'], u'байкал эм <b>1</b> <b>купить</b>')
        self.assertEqual(serp['sn'][9]['u'], 'http://alex-argo.ru/catalog/bioudobrenie-baykal-em-1-kupit.html')
        self.assertEqual(serp['sn'][9]['s'], None)

    def test4(self):
        html = self.get_data('captcha.html')
        captcha = MailRuParser(html).get_captcha_data()

        self.assertEqual(captcha['url'], 'http://go.mail.ru/ar_captcha?id=03f3380b2a979e6c')
        self.assertEqual(captcha['back'], u'https://go.mail.ru/search?q=test')
        self.assertEqual(captcha['q'], u'test')
        self.assertEqual(captcha['ajax'], u'1')
        self.assertEqual(captcha['sqid'], u'03f3380b2a979e6c')
        self.assertEqual(captcha['errback'], u'https://go.mail.ru/search?q=test&amp;frm=captcha_error')
        self.assertEqual(captcha['SequreWord'], None)

    def test5(self):
        html = self.get_data('2021-02-04.html')
        captcha = MailRuParser(html).get_captcha_data()

        self.assertEqual(captcha, None)

    def test6(self):
        html = self.get_data('2021-02-04-1.html')
        serp = MailRuParser(html).get_serp()

        self.assertEqual(serp['pc'], 445094)
        self.assertEqual(len(serp['sn']), 10)

        self.assertEqual(serp['sn'][0]['d'], 'lully.ru')
        self.assertEqual(serp['sn'][0]['p'], 1)
        self.assertEqual(serp['sn'][0]['t'], u'Главная')
        self.assertEqual(serp['sn'][0]['u'], 'http://www.lully.ru/')
        self.assertEqual(serp['sn'][0]['s'], u'Благодарим за понимание и надеемся на дальнейшее долгосрочное сотрудничество. Уважаемые покупатели и почитатели дизайн-<b>радиаторов</b> <b>Lully</b>.')

        self.assertEqual(serp['sn'][8]['d'], 'spbklimat.ru')
        self.assertEqual(serp['sn'][8]['p'], 9)
        self.assertEqual(serp['sn'][8]['t'], 'spbklimat.ru/upload/catalog_<b><b>lully</b></b>_for web_2.pdf')
        self.assertEqual(serp['sn'][8]['u'], 'http://www.spbklimat.ru/upload/catalog_lully_for%20web_2.pdf')
        self.assertEqual(serp['sn'][8]['s'], u'Дизайн-<b>радиаторы</b> «<b>Lully</b>» — что это? Больше всего дизайн-<b>радиаторы</b> напоминают элегантные декоративные панно.')

        self.assertEqual(serp['sn'][9]['d'], 'ru.all.biz')
        self.assertEqual(serp['sn'][9]['p'], 10)
        self.assertEqual(serp['sn'][9]['t'], u'<b>Радиаторы</b> <b>lully</b> в России. Сравнить цены и купить <b>Радиаторы</b> <b>Lully</b> на...')
        self.assertEqual(serp['sn'][9]['u'], 'http://ru.all.biz/radiatory-lully-cpk12388961')
        self.assertEqual(serp['sn'][9]['s'], u'<b>Радиаторы</b> <b>lully</b> купить в России по лучшим ценам. Заказывайте <b>Радиаторы</b> <b>Lully</b> прямо сейчас на сайте ru.all.biz')

    def test7(self):
        html = self.get_data('2021-02-04-2.html')
        serp = MailRuParser(html).get_serp()

        self.assertEqual(serp['pc'], 3513186)
        self.assertEqual(len(serp['sn']), 10)

        self.assertEqual(serp['sn'][0]['d'], 'xn--l1aafaekj4h.xn--p1ai')
        self.assertEqual(serp['sn'][0]['p'], 1)
        self.assertEqual(serp['sn'][0]['t'], u'<b>Купить</b> <b>мясо</b> <b>говядины</b> оптом в <b>Москве</b>')
        self.assertEqual(serp['sn'][0]['u'], u'http://xn--l1aafaekj4h.xn--p1ai/%D0%B3%D0%BE%D0%B2%D1%8F%D0%B4%D0%B8%D0%BD%D0%B0-%D0%BE%D0%BF%D1%82%D0%BE%D0%BC-%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C')
        self.assertEqual(serp['sn'][0]['s'], u'<b>Купить</b> <b>мясо</b> <b>говядины</b> оптом от 10 тонн в <b>Москве</b>. Поставки <b>говядины</b> по всей России. Мы занимаемся крупными поствками <b>мяса</b> от 10 тонн.')

        self.assertEqual(serp['sn'][9]['d'], 'moskva.meatinfo.ru')
        self.assertEqual(serp['sn'][9]['p'], 10)
        self.assertEqual(serp['sn'][9]['t'], u'<b>Купить</b> <b>говядину</b> <b>в</b> <b>Москве</b>')
        self.assertEqual(serp['sn'][9]['u'], u'http://moskva.meatinfo.ru/kupit\'_govyadinu')
        self.assertEqual(serp['sn'][9]['s'], u'<b>Купить</b> <b>говядину</b> <b>в</b> <b>Москве</b> - крупнейшая доска объявлений для специалистов рынка <b>мяса</b> и мясопродуктов.')


if __name__ == '__main__':
    unittest.main()

