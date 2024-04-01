def get_day_week(day):
    match day:
        case 1:
            return 'Sunday'
        case 2:
            return 'Monday'
        case 3:
            return 'Tuesday'
        case 4:
            return 'Wednesday'
        case 5:
            return 'Thursday'
        case 6:
            return 'Friday'
        case 7:
            return 'Saturday'
        case _:
            return '** Invalid **'
            
    
 
if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {get_day_week(day)}')
