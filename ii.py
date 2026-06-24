from typing import List
class LibraryBorrow:
    def __init__(self,id,reader_name, book_name, borrow_days,late_days,fine_per_day):
        self.id=id
        self.reader_name=reader_name
        self.book_name=book_name
        self.borrow_days=borrow_days
        self.late_days=late_days
        self.fine_per_day=fine_per_day
        self.total_fine=0
        self.fin_type=""
        
        self.calculate_fine()
        self.classify_fine()
        
    def calculate_fine(self):
        self.total_fine= self.late_days * self.fine_per_day
    def classify_fine(self):
        if self.total_fine >=200000:
            self.fin_type = "nang"
        elif self.total_fine >=50000:
            self.fin_type = "Trung binh"
        elif self.total_fine >0:
            self.fin_type = "nhe"
        else:
            self.fin_type = "khong phat"
class LibraryBorrowManager:
    def __init__(self):
        self.borrow_records : List [LibraryBorrow]=[]
        
    def show(self):
        if not self.borrow_records:
            print("danh sách đang rỗng")
            return
        print(f"{'Mã phiếu mượn':<18} | {'Họ tên bạn đọc':<25} | {'Tên sách':<20} | {'số ngày đã mượn':<18} | {'số ngày trễ hạn':<20} | {'tiền phạt mỗi ngày':<20} | {'Tổng tiền phạt':<15} | {'phân loại mức phạt':<20}")
        for i in self.borrow_records:
            print(f"{i.id:<18} | {i.reader_name:<25} | {i.book_name:<20} | {i.borrow_days:<18} | {i.late_days:<20} | {i.fine_per_day:<20} | {i.total_fine:<15} | {i.fin_type:<20}")
    def add(self):
        print("thêm")
        while True:
            id=input("nhập vào id: ")
            if not id:
                print("id không được để trống!")
                continue
            for i in self.borrow_records:
                if id== i.id:
                    print("đã bị trùng vui lòng nhập lại")
                    break
            else:
                    break
                
        while True:
            name = input("nhập vào tên bạn đọc")
            if not name:
                print("không đc để trống tên")
                continue
            break
        
        while True:
            name_book = input("nhập vào tên sách")
            if not name_book:
                print("không đc để trống tên")
                continue
            break
        
        while True:
            try:
                days= int(input("nhập vào số ngày mượn: "))
                if days<1 or days>365:
                    print("ngày phải nằm trong khoảng từ 1 - 365")
                    continue
                break
            except ValueError:
                print("nhập không hợp lệ")
                
        while True:
            try:
                late= int(input("nhập vào số ngày trễ: "))
                if late<0 or late>365:
                    print("ngày phải nằm trong khoảng từ 0 - 365")
                    continue
                if late >days:
                    print("số ngày trễ không đc lớn hơn số ngày mượn")
                    continue
                break
            except ValueError:
                print("nhập không hợp lệ")
                
        while True:
            try:
                per_day= float(input("nhập vào số tiền phạt mỗi ngày: "))
                if per_day<0:
                    print("tièn không đc âm")
                    continue
                break
            except ValueError:
                print("nhập không hợp lệ")
                
        new =LibraryBorrow(id, name, name_book, days,late, per_day)
        self.borrow_records.append(new)
        print("thêm thành công")
    def update(self):
            id= input("nhập mã id cần cập nhật")
            for i in self.borrow_records:
                if i.id== id:
                    print("đã tìm thấy tiếng hành cập nhật")
                    while True:
                        b_d = input("nhập vào số ngày mượn: ")
                        if not b_d:
                            b_day= i.borrow_days
                            break
                        try:
                            b_day= int(b_d)
                            if b_day<1 or b_day>365:
                                print("ngày phải nằm trong khoảng từ 1 - 365")
                                continue
                            break
                        except ValueError:
                            print("nhập không hợp lệ")
                    while True:
                        late = input("nhập vào số ngày trễ: ")
                        if not late:
                            late= i.late_days
                            break
                        try:
                            late= int(late)
                            if late<0 or late>365:
                                print("ngày phải nằm trong khoảng từ 0 - 365")
                                continue
                            break
                        except ValueError:
                            print("nhập không hợp lệ")
                    while True:
                        p_d = input("nhập vào số tiền trễ: ")
                        if not p_d:
                            p_d= i.fine_per_day
                            break
                        try:
                            p_d= float(p_d)
                            if p_d<0:
                                print("tièn không đc âm")
                                continue
                            break
                        except ValueError:
                            print("nhập không hợp lệ")
                    
                    i.borrow_days=b_day
                    i.late_days=late
                    i.fine_per_day=p_d
                    i.calculate_fine()
                    i.classify_fine()
                    print("cập nhật thành công")
                    break
            else:
                print("không thấy")
    def delete(self):
        did = input("nhập vào mã cần xóa")
        for i, p in enumerate(self.borrow_records):
            if p.id== did:
                comfirm=input("bạn có chắc muốn xóa(y/n): ").lower()
                match comfirm:
                    case "y": 
                        del self.borrow_records[i]
                        print("đã xóa thành công")
                    case "n":
                        print("đã hủy thao tác xóa")
                        break
                    case _:
                        print("lựa chọn không hợp lệ")
            else:
              print("không thấy phiếu cần xóa")
        
    def serch(self):  
        ser= input("nhập vào tên hoặc sách cần tìm: ").lower()
        if not ser:
            print("không được để trống")
        nneww = []
        for se in self.borrow_records :
            name_human= se.reader_name.lower()
            name_book= se.book_name.lower()
            if ser in name_human or ser in name_book:
                nneww.append(se)
        if not nneww:
            print("không tìm thấy ")
        else:
            print(f"{'Mã phiếu mượn':<18} | {'Họ tên bạn đọc':<25} | {'Tên sách':<20} | {'số ngày đã mượn':<18} | {'số ngày trễ hạn':<20} | {'tiền phạt mỗi ngày':<20} | {'Tổng tiền phạt':<15} | {'phân loại mức phạt':<20}")
            for ser in nneww:
                print(f"{se.id:<18} | {se.reader_name:<25} | {se.book_name:<20} | {se.borrow_days:<18} | {se.late_days:<20} | {se.fine_per_day:<20} | {se.total_fine:<15} | {se.fin_type:<20}")
                
            
        
            
        
            
def menu():
    print("""
          ====================menu====================
          1. Hiển thi danh sách phiếu mượn
          2. thêm phiếu mượn mới
          3.cập nhật phiếu mượn
          4.Xóa phiếu mượn
          5. Tìm kiếm phiếu mượn
          6.thoát
          ============================================
          """)
    
def main():
    manager =LibraryBorrowManager()
    while True:
        menu()
        choice= input("mời bạn nhập lựa chọn: ")
        match choice:
            case"1":
                manager.show()
            case"2":
                manager.add()
            case"3":
                manager.update()
            case"4":
                manager.delete()
            case"5":
                manager.serch()
            case"6":
                print("cảm on đã sử dụng chương trình")
                break
            case _:
                print("lựa chọn không hợp lệ")
if __name__ == "__main__":
    main()
                
            
        