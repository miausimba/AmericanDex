from typing import TYPE_CHECKING

from .cog import Config

if TYPE_CHECKING:
    from universedex.core.bot import UniverseDexBot


async def setup(bot: "UniverseDexBot"):
    await bot.add_cog(Config(bot))
