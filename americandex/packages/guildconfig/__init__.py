from typing import TYPE_CHECKING

from .cog import Config

if TYPE_CHECKING:
    from americandex.core.bot import AmericanDexBot


async def setup(bot: "AmericanDexBot"):
    await bot.add_cog(Config(bot))
