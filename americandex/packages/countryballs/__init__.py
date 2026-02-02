from typing import TYPE_CHECKING

from .cog import CountryBallsSpawner

if TYPE_CHECKING:
    from americandex.core.bot import AmericanDexBot


async def setup(bot: "AmericanDexBot"):
    cog = CountryBallsSpawner(bot)
    await bot.add_cog(cog)
    await cog.load_cache()
