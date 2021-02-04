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


if __name__ == '__main__':
    unittest.main()

