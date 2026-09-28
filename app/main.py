from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    # 1. Куплюка продуктов в баре
    cinema_bar = CinemaBar()
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        cinema_bar.sell_product(
            customer=customer,
            product=customer.food
        )

    # 2. Создание списка клиентов для зала и уборщика
    hall_customers = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]
    cleaning_staff = Cleaner(name=cleaner)

    # 3. Запуск киносеанса (передаем number=hall_number)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=hall_customers,
        cleaning_staff=cleaning_staff
    )
