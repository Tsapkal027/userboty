################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from Mix import *

__modles__ = "sudo"
__help__ = """
 Help Command Sudo

• Perintah: <code>{0}addsudo</code> [reply user]
• Penjelasan: Untuk menambahkan pengguna sudo.

• Perintah: <code>{0}delsudo</code> [reply user]
• Penjelasan: Untuk menghapus pengguna sudo.

• Perintah: <code>{0}sudolist</code>
• Penjelasan: Untuk melihat daftar sudo.
"""


@ky.ubot("addsudo", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    msg = await m.reply(f"{emo.proses} <b>Processing...</b>")
    user_id = await c.extract_user(m)
    if not user_id:
        return await msg.edit(
            f"{emo.gagal} <b>Silakan balas pesan pengguna/username/user id</b>"
        )
    try:
        user = await c.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")

    if user.id in sudo_users:
        return await msg.edit(
            f"{emo.sukses} <b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Sudah menjadi pengguna sudo.</b>"
        )

    try:
        udB.add_to_var(c.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(
            f"{emo.sukses} <b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Ditambahkan ke pengguna sudo.</b>"
        )
    except Exception as error:
        return await msg.edit(error)


@ky.ubot("delsudo", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    msg = await m.reply(f"{emo.proses} <b>Processing...</b>")
    user_id = await c.extract_user(m)
    if not user_id:
        return await m.reply(
            f"{emo.gagal} <b>Silakan balas pesan penggjna/username/user id.</b>"
        )

    try:
        user = await c.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")

    if user.id not in sudo_users:
        return await msg.edit(
            f"{emo.gagal} <b>{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Bukan bagian pengguna sudo.</b>"
        )

    try:
        udB.remove_from_var(c.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(
            f"{emo.sukses} <b>[{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Dihapus dari pengguna sudo.</b>"
        )
    except Exception as error:
        return await msg.edit(error)


@ky.ubot("sudolist", sudo=True)
async def _(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    msg = await m.reply(f"{emo.proses} <b>Processing...</b>")
    sudo_users = udB.get_list_from_var(c.me.id, "SUDO_USER", "ID_NYA")

    if not sudo_users:
        return await msg.edit(f"{emo.gagal} <b>Tidak ada pengguna sudo ditemukan.</b>")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await c.get_users(int(user_id))
            sudo_list.append(
                f" {emo.profil} • [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code>"
            )
        except:
            continue

    if sudo_list:
        response = (
            f"{emo.alive} <b>Daftar Pengguna:</b>\n"
            + "\n".join(sudo_list)
            + f"\n<b> • </b> <code>{len(sudo_list)}</code>"
        )
        return await msg.edit(response)
    else:
        return await msg.edit("<b>Eror</b>")
