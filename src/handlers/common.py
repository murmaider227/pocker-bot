from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters import CommandObject


router = Router()


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message, command: CommandObject):
    await message.answer(command.args)
