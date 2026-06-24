from typing import List

class Vehicle:
    def __init__ (self, id, vehicle_name, license_plate,base_maintenance_fee, kilometers, cost_per_km):
        self.id=id
        self.vehicle_name=vehicle_name
        self.license_plate=license_plate
        self.base_maintenance_fee=base_maintenance_fee
        self.kilometers= kilometers
        self.cost_per_km=cost_per_km
        self.total_maintenance_cost=0
        self.maintenance_type=""
        self.calculate_maintenance_cost()
        self.classify_maintenance()
    def calculate_maintenance_cost(self):
        self.total_maintenance_cost = self.base_maintenance_fee +self.kilometers*self.cost_per_km
    def classify_maintenance(self)     :
        if self.total_maintenance_cost >15000000:
            self.maintenance_type="rat cao"
        elif self.total_maintenance_cost >=5000000:
            self.maintenance_type="cao"
        elif self.total_maintenance_cost >=1000000:
            self.maintenance_type="trung binh"
        else:
            self.maintenance_type="thap"
            
class VehicleManager:
    def __init__(self):
        self.vehicles: List[Vehicle]=[]
    def show(self):
        if not  self.vehicles:
            print("danh sách đang rỗng")
            return
        print(f"{'Mã phương tiện':<15} | {'tên phương tiện':<15} | {'biển số xe':<20} | {'phí bảo trì cố định':<20} | {'số km đã đi':<15} | {'chi phí/ km':<15} | {' Tổng chi phí bảo trì':<20} | {'Phân loại chi phí':<20}")
        for i in self.vehicles:
            print(f"{i.id:<15} | {i.vehicle_name:<15} | {i.license_plate:<20} | {i.base_maintenance_fee:<20} | {i.kilometers:<15} | {i.cost_per_km:<15} | {i.total_maintenance_cost:<20} | {i.maintenance_type:<20}")
    def add(self):
        while True:
            id= input("nhập vào mã phương tiện")
            if not id :
                print("mã d không đc để rỗng")
                continue
            for i in self.vehicles:
                if i.id==id:
                    print("mã sản phẩm không được trùng")
                    break
            else:
                break
        
        while True:
            name = input("nhập vào tên phương tiện: ")
            if not name:
                print("không đc để trống")
                continue
            break
        
        while True:
            number_ve= input("nhập vào biển số xe")
            if not number_ve:
                print("biển xe không đc rỗng")
                continue
            for i in self.vehicles:
                if i.license_plate==id:
                    print("biển số không được trùng")
                    break
            else:
                break
            
        while True:
            try:
                fee=float(input("nhập vào phí bảo trì: "))
                if fee <= 0:
                    print("phí bảo trì phải lớn hơn 0")
                    continue
                break
            except ValueError:
                print("nhập không hợp lệ")
                
        while True:
            try:
                km=float(input("nhập vào km đã đi: "))
                if km < 0:
                    print("km phải lớn hơn= 0")
                    continue
                break
            except ValueError:
                print("nhập không hợp lệ")
                
        while True:
            try:
                per_km=float(input("nhập vào phí bảo trì mỗi km: "))
                if per_km <= 0:
                    print("phí bảo trì phải lớn hơn 0")
                    continue
                break
            except ValueError:
                print("nhập không hợp lệ")
            
        new= Vehicle(id, name, number_ve, fee, km, per_km)
        self.vehicles.append(new)
        print("đã thêm thành công")
        
    def update(self):
        while True:
            id= input("nhập vào mã cần cập nhật: ")
            if not id :
                print("mã không được để trống")
                continue
            for i in self.vehicles:
                if id == i.id:
                    print("đã tìm thấy mã tiến hnhf cập nhật")
                    while True:
                        fee= input("nhập vào phí bảo trì cố định ")
                        if not fee:
                            fe= i.base_maintenance_fee
                            break
                        try:
                            fe= float(fee)
                            if fe <= 0:
                                print("phí bảo trì phải lớn hơn 0")
                                continue
                            break
                        except ValueError:
                            print("nhập không hợp lệ")
                            
                    while True:
                        km = input("nhập số km đã đi:")
                        if not km:
                            km_run = i.kilometers
                            break
                        try:
                            km_run = input(km)
                            if km_run < 0:
                                print("km phải lớn hơn= 0")
                                continue
                            break
                        except ValueError:
                            print("nhập không hợp lệ")
                            
                    while True:
                        per_km= input("nhập vào phí bảo trì mỗi km ")
                        if not per_km:
                            per= i.base_maintenance_fee
                            break
                        try:
                            per= float(per_km)
                            if per <= 0:
                                print("phí bảo trì phải lớn hơn 0")
                                continue
                            break
                        except ValueError:
                            print("nhập không hợp lệ")
                            
                    i.base_maintenance_fee= fe
                    i.kilometers=km_run
                    i.cost_per_km=per
                    i.calculate_maintenance_cost()
                    i.classify_maintenance()
                    print("cập nhật phương tiện thành công")
                    break
            else:
                print("không tìm thấy")
                break
            break
        
    def delete(self):
        while True:
            dele = input("nhập vào mã phương tiện cần xóa")
            if not dele:
                print("không để trống")
                continue
            for i in  self.vehicles:
                if i.id==dele:
                    confirm= input("bạn có chắc muốn xóa không(y/n) ").lower()
                    match confirm:
                        case "y":
                            self.vehicles.remove(i)
                            print("đã xóa")
                        case "n":
                            print("đã huy thao tác")
                            break
                        case _:
                            print("lựa chọn không hợp lệ")
                            break
                else:
                    break
            print("không tìm thấy cần xóa")
            break
                        
                        
                    
        
            
def menu():
    print("""
          ===============Menu===============
          1. Hiển thị danh sách phương tiện
          2. Thêm phương tiện mới
          3. Cập nhật phương tiện
          4. Xóa phương tiện
          5. Tìm kiếm phương tiện
          6. Thoát
          """
          )
def main():
    manager=  VehicleManager()
    while True:
        menu()
        choice= input("nhập vào lựa chọn của bạn: ")
        match choice:
            case "1":
                manager.show()
            case "2":
                manager.add()
            case "3":
                manager.update()
            case "4":
                manager.delete()
            case "5":
                pass
            case "6":
                print("cảm ơn đã xử dụng chương trình")
                break
            case _:
                print("lựa chọn không hợp lệ")
if __name__ == "__main__":
    main()