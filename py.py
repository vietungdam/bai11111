from typing import List

# Lớp đại diện cho một đối tượng phiếu mượn sách
class LibraryBorrow:
    def __init__(self, id, reader_name, book_name, borrow_days, late_days, fine_per_day):
        # Gán các giá trị đầu vào thành thuộc tính
        self.id = id
        self.reader_name = reader_name
        self.book_name = book_name
        self.borrow_days = borrow_days
        self.late_days = late_days
        self.fine_per_day = fine_per_day
        self.total_fine = 0
        self.fine_type = ''
        
        # Tự động tính toán tiền phạt và xếp loại ngay khi đối tượng được tạo
        self.calculate_fine()
        self.classify_fine()
        
    # Hàm tính tổng tiền phạt
    def calculate_fine(self):
        if self.late_days == 0:
            self.total_fine = 0
        else:
            self.total_fine = self.late_days * self.fine_per_day
    
    # Hàm phân loại mức phạt dựa trên tổng tiền
    def classify_fine(self):
        if self.total_fine >= 200000:
            self.fine_type = 'Nặng'
        elif self.total_fine >= 50000:
            self.fine_type = 'Trung bình'
        elif self.total_fine > 0:
            self.fine_type = 'Nhẹ'
        else:  
            self.fine_type = 'Không phạt'


# Lớp chứa các nghiệp vụ quản lý danh sách phiếu mượn
class LibraryBorrowManager:
    def __init__(self):
        # Khởi tạo danh sách và nạp sẵn 5 dữ liệu mẫu
        self.borrow_records: List[LibraryBorrow] = [

        ]
        
    # Chức năng 1: Hiển thị danh sách phiếu mượn dưới dạng bảng
    def display_records(self):
        if not self.borrow_records:
            print("\nDanh sách phiếu mượn đang rỗng!")
            return
            
        print(f"\n{'Mã PM':<10} | {'Họ tên':<20} | {'Tên sách':<22} | {'Ngày mượn':<10} | {'Ngày trễ':<10} | {'Phạt/Ngày':<10} | {'Tổng phạt':<15} | {'Mức phạt'}")
        print("-" * 125)
        for pro in self.borrow_records:
            print(f"{pro.id:<10} | {pro.reader_name:<20} | {pro.book_name:<22} | {pro.borrow_days:<10} | {pro.late_days:<10} | {pro.fine_per_day:<10} | {pro.total_fine:<15} | {pro.fine_type}")

    # Chức năng 2: Thêm một phiếu mượn mới
    def add_record(self):
        # Vòng lặp nhập mã phiếu mượn
        while True:
            pro_id = input("Nhập vào mã phiếu mượn: ").strip()
            if not pro_id:
                print("Mã phiếu mượn không được để trống!")
                continue
            
            # Kiểm tra mã trùng bằng cấu trúc for...else
            for p in self.borrow_records:
                if p.id == pro_id:
                    print("Mã phiếu mượn đã tồn tại, vui lòng nhập lại!")
                    break # Nếu trùng ID, thoát for và chạy lại vòng while
            else:
                # Khối else này chỉ chạy khi vòng for duyệt hết mà KHÔNG gặp lệnh break
                # (nghĩa là ID không bị trùng), ta sẽ dùng break để thoát vòng lặp while True
                break

        # Vòng lặp nhập họ tên
        while True:     
            pro_name = input("Nhập vào họ tên bạn đọc: ").strip()
            if not pro_name:
                print("Họ tên không được để trống!")
                continue
            break
            
        # Vòng lặp nhập tên sách
        while True:     
            b_name = input("Nhập vào tên sách: ").strip()
            if not b_name:
                print("Tên sách không được để trống!")
                continue
            break

        # Vòng lặp nhập và kiểm tra ngày mượn
        while True:
            try:
                borrow_days = int(input("Nhập vào số ngày đã mượn (1-365): "))
                if borrow_days < 1 or borrow_days > 365:
                    print("Số ngày mượn phải nằm trong khoảng từ 1 đến 365!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")

        # Vòng lặp nhập và kiểm tra ngày trễ
        while True:
            try:
                late_days = int(input("Nhập vào số ngày trễ hạn (0-365): "))
                if late_days < 0 or late_days > 365:
                    print("Số ngày trễ hạn phải nằm trong khoảng từ 0 đến 365!")
                    continue
                if late_days >= borrow_days:
                    print("Số ngày trễ hạn không được lớn hơn số ngày đã mượn!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")

        # Vòng lặp nhập và kiểm tra tiền phạt
        while True:
            try:
                fine_per_day = int(input("Nhập vào tiền phạt mỗi ngày trễ: "))
                if fine_per_day < 0:
                    print("Tiền phạt không được là số âm!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")

        # Khởi tạo và đẩy đối tượng mới vào danh sách
        new_record = LibraryBorrow(pro_id, pro_name, b_name, borrow_days, late_days, fine_per_day)
        self.borrow_records.append(new_record)  
        print("Thêm phiếu mượn thành công!")   

    # Chức năng 3: Cập nhật thông tin phiếu mượn
    def update_record(self):
        pid = input("Nhập mã phiếu mượn cần cập nhật: ").strip()
        
        # Duyệt tìm phiếu mượn bằng cấu trúc for...else
        for order_to_update in self.borrow_records:
            if order_to_update.id == pid:
                # Cập nhật số ngày đã mượn
                while True:
                    b_str = input(f"Số ngày đã mượn ({order_to_update.borrow_days}): ").strip()
                    if not b_str: # Giữ nguyên giá trị cũ nếu bỏ trống
                        borrow_days = order_to_update.borrow_days
                        break
                    try:
                        borrow_days = int(b_str)
                        if borrow_days < 1 or borrow_days > 365:
                            print("Số ngày mượn phải từ 1 đến 365!")
                            continue
                        break
                    except ValueError:
                        print("Vui lòng nhập một số hợp lệ!")

                # Cập nhật số ngày trễ
                while True:
                    l_str = input(f"Số ngày trễ hạn ({order_to_update.late_days}): ").strip()
                    if not l_str:
                        late_days = order_to_update.late_days
                        if late_days > borrow_days:
                            print("Số ngày trễ hiện tại đang lớn hơn số ngày mượn mới. Vui lòng nhập lại số ngày trễ!")
                            continue
                        break
                    try:
                        late_days = int(l_str)
                        if late_days < 0 or late_days > 365:
                            print("Số ngày trễ phải từ 0 đến 365!")
                            continue
                        if late_days > borrow_days:
                            print("Số ngày trễ không được lớn hơn số ngày đã mượn!")
                            continue
                        break
                    except ValueError:
                        print("Vui lòng nhập một số hợp lệ!")

                # Cập nhật tiền phạt
                while True:
                    f_str = input(f"Tiền phạt mỗi ngày ({order_to_update.fine_per_day}): ").strip()
                    if not f_str:
                        fine_per_day = order_to_update.fine_per_day
                        break
                    try:
                        fine_per_day = int(f_str)
                        if fine_per_day < 0:
                            print("Tiền phạt không được âm!")
                            continue
                        break
                    except ValueError:
                        print("Vui lòng nhập một số hợp lệ!")
                        
                # Gán giá trị mới và tính toán lại
                order_to_update.borrow_days = borrow_days
                order_to_update.late_days = late_days
                order_to_update.fine_per_day = fine_per_day
                order_to_update.calculate_fine()
                order_to_update.classify_fine()
                
                print("Cập nhật phiếu mượn thành công!")
                break # Cập nhật xong thì thoát vòng for
            else:
            # Khối else của for: Chạy khi duyệt hết danh sách mà không tìm thấy ID (không bị break)
              print("Không tìm thấy phiếu mượn cần cập nhật!")

    # Chức năng 4: Xóa phiếu mượn theo ID
    def delete_record(self):
        pid = input("Nhập mã phiếu mượn cần xóa: ").strip()
        # Dùng enumerate để lấy cả vị trí (i) và đối tượng (p)
        for i, p in enumerate(self.borrow_records):
            if p.id == pid:
                confirm = input("Bạn có chắc muốn xóa phiếu mượn này không? (Y/N): ").strip().lower()
                if confirm == 'y':
                    del self.borrow_records[i] # Xóa khỏi mảng
                    print("Xóa phiếu mượn thành công!")
                elif confirm == 'n':
                    print("Đã hủy thao tác xóa!")
                else:
                    print("Lựa chọn không hợp lệ!")
                return
        print("Không tìm thấy phiếu mượn cần xóa!")

    # Chức năng 5: Tìm kiếm theo tên hoặc tên sách
    def search_record(self):
        # Chuyển từ khóa về dạng viết thường
        keyword = input("Nhập từ khóa tìm kiếm (tên bạn đọc/tên sách): ").strip().lower()
        
        results = []
        
        for pro in self.borrow_records:
            ten_ban_doc = pro.reader_name.lower()
            ten_sach = pro.book_name.lower()
            
            # Kiểm tra xem từ khóa có nằm trong tên độc giả HOẶC tên sách không
            if keyword in ten_ban_doc or keyword in ten_sach:
                results.append(pro)
        
        if not results:
            print("Không tìm thấy phiếu mượn phù hợp!")
        else:
            
            print(f"\nKết quả tìm kiếm cho '{keyword}':")
            print(f"{'Mã PM':<10} | {'Họ tên':<20} | {'Tên sách':<22} | {'Ngày mượn':<10} | {'Ngày trễ':<10} | {'Phạt/Ngày':<10} | {'Tổng phạt':<15} | {'Mức phạt'}")
            print("-" * 125)
            for pro in results:
                print(f"{pro.id:<10} | {pro.reader_name:<20} | {pro.book_name:<22} | {pro.borrow_days:<10} | {pro.late_days:<10} | {pro.fine_per_day:<10} | {pro.total_fine:<15} | {pro.fine_type}")

# Hiển thị giao diện menu
def menu():
    print("\n================ MENU ================")
    print("1. Hiển thị danh sách phiếu mượn")
    print("2. Thêm phiếu mượn mới")
    print("3. Cập nhật phiếu mượn")
    print("4. Xóa phiếu mượn")
    print("5. Tìm kiếm phiếu mượn")
    print("6. Thoát")
    print("=====================================")

# Hàm điều khiển luồng chính
def main():
    manager = LibraryBorrowManager()
    while True: 
        menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()
        # Dùng match-case điều hướng menu
        match choice:
            case '1':
                manager.display_records()
            case '2':
                manager.add_record()
            case '3':
                manager.update_record()
            case '4':
                manager.delete_record()
            case '5':
                manager.search_record()
            case '6':
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý thư viện!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6!")

# Đảm bảo mã chỉ thực thi khi chạy trực tiếp file này
if __name__ == "__main__":
    main()