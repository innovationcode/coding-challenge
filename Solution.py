def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
      
      if D1 + D2 + D3 == 0:
            return 0
      
      if R1 < 0 or R2 < 0 or R3 < 0:
            return -1

      if D1 < 0 or D2 < 0 or D3 < 0:
            return -1

      day = 0
      pending = K
      total_rate = 0
      number_of_power_day = 0
      d1_added = False
      d2_added = False
      d3_added = False
      
      while pending > 0:
            day += 1
            if D1 <= day and not d1_added:
                  total_rate += R1
                  d1_added = True
            if D2 <= day and not d2_added:
                  total_rate += R2
                  d2_added = True
            if D3 <= day and not d3_added:
                  total_rate += R3
                  d3_added = True
            if total_rate == 0:
                  continue
            else:
                  pending = pending - total_rate
                  if pending >= 0:
                        number_of_power_day += 1

      return number_of_power_day    
    
