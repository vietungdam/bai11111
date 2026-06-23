from typing import List

class DeliveryOrder:
    def __init__(self, order_id, receiver_name, base_fee, distance, surcharge):
        self.order_id = order_id
        self.receiver_name = receiver_name
        self.base_fee = base_fee
        self.distance = distance
        self.surcharge = surcharge
        self.total_delivery_cost = 0.0
        self.delivery_status = ''
        
        self.calculate_total_cost()
        self.classify_delivery_status()
        
    def calculate_total_cost(self):
        self.total_delivery_cost = (self.base_fee * self.distance) + self.surcharge
    
    def classify_delivery_status(self):
        if self.total_delivery_cost > 600000:
            self.delivery_status = 'Đặc biệt'
        elif self.total_delivery_cost > 300000:
            self.delivery_status = 'Đường dài'
        elif self.total_delivery_cost > 100000:
            self.delivery_status = 'Cận tỉnh'
        else:  
            self.delivery_status = 'Tiêu chuẩn'


class OrderManager:
    def __init__(self):
        self.orders: List[DeliveryOrder] = []
        
    def display_orders(self):
        if not self.orders:
            print("\nroongx.")
            return
            
        print(f"\n{'Mã Đơn':<10} | {'Tên người nhận':<20} | {'Cước nền':<10} | {'Khoảng cách':<12} | {'Phụ phí':<10} | {'Tổng chi phí':<15} | {'Trạng thái đơn'}")
        print("-" * 110)
        for pro in self.orders:
            print(f"{pro.order_id:<10} | {pro.receiver_name:<20} | {pro.base_fee:<10.1f} | {pro.distance:<12} | {pro.surcharge:<10.1f} | {pro.total_delivery_cost:<15.1f} | {pro.delivery_status}")

    def add_order(self):
        while True:
            pro_id = input("Nhập vào mã : ").strip()
            if not pro_id:
                print("không được để trống!")
                continue
            
            is_duplicate = any(p.order_id == pro_id for p in self.orders)
            if is_duplicate:
                print(" đã tồn tại, vui lòng nhập lại!")
                continue
            break

        while True:     
            pro_name = input("Nhập vào tên  ").strip()
            if not pro_name:
                print(" không được để trống!")
                continue
            break

        while True:
            try:
                fee = float(input("Nhập vào cước nền: "))
                if fee < 0:
                    print("Cước nền không được là số âm!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")

        while True:
            try:
                distance = int(input("Nhập vào khoảng cách (km): "))
                if distance < 1 or distance > 5000:
                    print("Khoảng cách phải nằm trong khoảng từ 1 đến 5000!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")

        while True:
            try:
                surcharge = float(input("Nhập vào phụ phí: "))
                if surcharge < 0:
                    print("Phụ phí không được là số âm!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")

        new_order = DeliveryOrder(pro_id, pro_name, fee, distance, surcharge)
        self.orders.append(new_order)  
        print("Đã thêm vận đơn thành công!")   

    def update_order(self):
        pid = input("Nhập mã vận đơn cần cập nhật: ").strip()
        order_to_update = next((p for p in self.orders if p.order_id == pid), None)
               
        if not order_to_update:
            print("Không tìm thấy ")
            return
        pro_name = input(f"Tên người nhận ({order_to_update.receiver_name}): ").strip()
        if not pro_name:
            pro_name = order_to_update.receiver_name

        while True:
            fee_str = input(f"Cước nền ({order_to_update.base_fee}): ").strip()
            if not fee_str:
                fee = order_to_update.base_fee
                break
            try:
                fee = float(fee_str)
                if fee < 0:
                    print(" không được âm!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")

        while True:
            dist_str = input(f"Khoảng cách ({order_to_update.distance}): ").strip()
            if not dist_str:
                distance = order_to_update.distance
                break
            try:
                distance = int(dist_str)
                if distance < 1 or distance > 5000:
                    print("Khoảng cách phải từ 1 đến 5000!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")

        while True:
            sur_str = input(f"Phụ phí ({order_to_update.surcharge}): ").strip()
            if not sur_str:
                surcharge = order_to_update.surcharge
                break
            try:
                surcharge = float(sur_str)
                if surcharge < 0:
                    print(" không được âm!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")
                
        order_to_update.receiver_name = pro_name
        order_to_update.base_fee = fee
        order_to_update.distance = distance
        order_to_update.surcharge = surcharge
        order_to_update.calculate_total_cost()
        order_to_update.classify_delivery_status()
        
        print("Đã cập nhật !")

    def delete_order(self):
        pid = input("Nhập mã ").strip()
        for i, p in enumerate(self.orders):
            if p.order_id == pid:
                confirm = input(" (y/n): ").strip().lower()
                if confirm == 'y':
                    del self.orders[i]
                    print("Đã xóa !")
                else:
                    print("Đã hủy thao tác xóa.")
                return
        print("Không tìm thấy ")

    def search_order(self):
        name = input("Nhập tên cần tìm kiếm: ").strip().lower()
        found = False
        
        for pro in self.orders:
            if name in pro.receiver_name.lower():
                if not found:
                    print(f"\nKết quả tìm kiếm cho '{name}':")
                    print(f"{'Mã Đơn':<10} | {'Tên người nhận':<20} | {'Cước nền':<10} | {'Khoảng cách':<12} | {'Phụ phí':<10} | {'Tổng chi phí':<15} | {'Trạng thái đơn'}")
                    print("-" * 110)
                    
                print(f"{pro.order_id:<10} | {pro.receiver_name:<20} | {pro.base_fee:<10.1f} | {pro.distance:<12} | {pro.surcharge:<10.1f} | {pro.total_delivery_cost:<15.1f} | {pro.delivery_status}")
                found = True
                
        if not found:
            print("Không tìm thấy ")

def menu():
    print("\n================ MENU ================")
    print("1. Hiển thị danh sách vận đơn trong hệ thống")
    print("2. Nhập vận đơn mới")
    print("3. Cập nhật thông tin vận đơn")
    print("4. Xóa vận đơn khỏi hệ thống")
    print("5. Tìm kiếm vận đơn theo tên người nhận")
    print("6. Thoát")
    print("======================================")

def main():
    manager = OrderManager()
    while True: 
        menu()
        choice = input("Mời bạn nhập lựa chọn: ").strip()
        match choice:
            case '1':
                manager.display_orders()
            case '2':
                manager.add_order()
            case '3':
                manager.update_order()
            case '4':
                manager.delete_order()
            case '5':
                manager.search_order()
            case '6':
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vận đơn!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại!")

if __name__ == "__main__":
    main()