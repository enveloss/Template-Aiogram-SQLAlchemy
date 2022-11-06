from typing import Any, Tuple
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types

class Config:
    get_lang = None

class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user = types.User.get_current()
        return await Config.get_lang(user.id)

def setup_middleware(dp, get_lang, locales_dir, i18n_domain='bot'):
    Config.get_lang = get_lang
    i18n = ACLMiddleware(i18n_domain, locales_dir)
    dp.middleware.setup(i18n)
    return i18n