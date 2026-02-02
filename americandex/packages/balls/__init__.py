from typing import TYPE_CHECKING

from .cog import Balls

if TYPE_CHECKING:
    from americandex.core.bot import AmericanDexBot


async def setup(bot: "AmericanDexBot"):
    await bot.add_cog(Balls(bot))
