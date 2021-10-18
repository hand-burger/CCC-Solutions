n = input()

l_count = n.count('L')
m_count = n.count("M")

l_position = n[0:l_count]
m_position = n[l_count:l_count + m_count]
ls_out_of_place = l_count - l_position.count("L")
ms_out_of_place = m_count - m_position.count("M")


print(ls_out_of_place + ms_out_of_place -
      min(l_position.count("M"), m_position.count("L")))
