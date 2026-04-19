has_ticket = True
is_vip = False
is_early  = True

if  not is_vip or (not has_ticket and not is_early):
    print("Enjoy the show!!")
else:
    print("No entry.")