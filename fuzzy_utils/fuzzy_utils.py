import factory

from factory import fuzzy
from factory.fuzzy import BaseFuzzyAttribute


class FuzzyColor(BaseFuzzyAttribute):
    def fuzz(self):
        color = lambda: fuzzy._random.randint(0, 255)
        return '#%02X%02X%02X' % (color(), color(), color())


class FuzzyEmail(fuzzy.BaseFuzzyAttribute):
    domanins = ['it', 'co.uk', 'com']

    # thanks to https://github.com/mailcheck/mailcheck/wiki/List-of-Popular-Domains
    common_email_providers = [
        'aol.com', 'att.net', 'comcast.net', 'facebook.com', 'gmail.com', 'gmx.com', 'googlemail.com',
        'google.com', 'hotmail.com', 'hotmail.co.uk', 'mac.com', 'me.com', 'mail.com', 'msn.com',
        'live.com', 'sbcglobal.net', 'verizon.net', 'yahoo.com', 'yahoo.co.uk',
        'email.com', 'games.com', 'gmx.net', 'hush.com', 'hushmail.com', 'icloud.com', 'inbox.com',
        'lavabit.com', 'love.com', 'outlook.com', 'pobox.com', 'rocketmail.com',
        'safe-mail.net', 'wow.com', 'ygm.com', 'ymail.com', 'zoho.com', 'fastmail.fm', 'yandex.com',
        'bellsouth.net', 'charter.net', 'comcast.net', 'cox.net', 'earthlink.net', 'juno.com',
        'btinternet.com', 'virginmedia.com', 'blueyonder.co.uk', 'freeserve.co.uk', 'live.co.uk',
        'ntlworld.com', 'o2.co.uk', 'orange.net', 'sky.com', 'talktalk.co.uk', 'tiscali.co.uk',
        'virgin.net', 'wanadoo.co.uk', 'bt.com',
        'sina.com', 'qq.com', 'naver.com', 'hanmail.net', 'daum.net', 'nate.com', 'yahoo.co.jp',
        'yahoo.co.kr', 'yahoo.co.id', 'yahoo.co.in', 'yahoo.com.sg', 'yahoo.com.ph',
        'hotmail.fr', 'live.fr', 'laposte.net', 'yahoo.fr', 'wanadoo.fr', 'orange.fr', 'gmx.fr',
        'sfr.fr', 'neuf.fr', 'free.fr',
        'gmx.de', 'hotmail.de', 'live.de', 'online.de', 't-online.de', 'web.de', 'yahoo.de',
        'mail.ru', 'rambler.ru', 'yandex.ru', 'ya.ru', 'list.ru',
        'hotmail.be', 'live.be', 'skynet.be', 'voo.be', 'tvcablenet.be', 'telenet.be',
        'hotmail.com.ar', 'live.com.ar', 'yahoo.com.ar', 'fibertel.com.ar', 'speedy.com.ar', 'arnet.com.ar',
        'hotmail.com', 'gmail.com', 'yahoo.com.mx', 'live.com.mx', 'yahoo.com', 'hotmail.es', 'live.com',
        'hotmail.com.mx', 'prodigy.net.mx', 'msn.com'
    ]

    def __init__(self, user_part_length=30, domain_part_length=30, use_common_providers=True):
        self.fuzzy_user_part = fuzzy.FuzzyText(length=user_part_length)
        self.fuzzy_domain_part = fuzzy.FuzzyText(length=domain_part_length)
        self.use_common_providers = use_common_providers

    def fuzz(self):
        if self.use_common_providers:
            domain = self.common_email_providers[fuzzy._random.randint(0, len(self.common_email_providers) - 1)]
        else:
            domain = self.fuzzy_domain_part.fuzz() + '.' + self.domanins[fuzzy._random.randint(0, len(self.domanins) - 1)]

        return self.fuzzy_user_part.fuzz() + '@' + domain
