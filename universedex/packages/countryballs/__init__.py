from typing import TYPE_CHECKING

from .cog import CountryBallsSpawner

if TYPE_CHECKING:
    from universedex.core.bot import UniverseDexBot


async def setup(bot: "UniverseDexBot"):
    cog = CountryBallsSpawner(bot)
    await bot.add_cog(cog)
    await cog.load_cache()
