from typing import TYPE_CHECKING

from .cog import Player

if TYPE_CHECKING:
    from universedex.core.bot import UniverseDexBot


async def setup(bot: "UniverseDexBot"):
    await bot.add_cog(Player(bot))
