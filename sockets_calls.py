from sockets import notify
def notify_both(lost_user_id, found_user_id, item_title, item_type):
    notify(lost_user_id, {"item": item_title, "type": item_type})
    notify(found_user_id, {"item": item_title, "type": item_type})
