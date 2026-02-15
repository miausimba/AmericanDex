from typing import TYPE_CHECKING

from .cog import Info

if TYPE_CHECKING:
    from universedex.core.bot import UniverseDexBot


async def setup(bot: "UniverseDexBot"):
    await bot.add_cog(Info(bot))
