import Link from "next/link";
import TableUsers from "./TableUsers";

const test_data = [
    {
        "user_id": 1001,
        "username": "ivanov_alex",
        "first_name": "Александр",
        "last_name": "Иванов",
        "created_at": "2023-06-15T10:30:00Z",
        "last_activity": "2024-01-22T14:45:00Z"
    },
    {
        "user_id": 1002,
        "username": "petrova_maria",
        "first_name": "Мария",
        "last_name": "Петрова",
        "created_at": "2023-08-22T09:15:00Z",
        "last_activity": "2024-01-21T11:20:00Z"
    },
    {
        "user_id": 1003,
        "username": "sidorov_ivan",
        "first_name": "Иван",
        "last_name": "Сидоров",
        "created_at": "2023-11-10T16:45:00Z",
        "last_activity": "2024-01-20T09:30:00Z"
    },
    {
        "user_id": 1004,
        "username": "smirnova_ekaterina",
        "first_name": "Екатерина",
        "last_name": "Смирнова",
        "created_at": "2024-01-05T14:20:00Z",
        "last_activity": "2024-01-22T16:10:00Z"
    },
    {
        "user_id": 1005,
        "username": "kuznetsov_dmitry",
        "first_name": "Дмитрий",
        "last_name": "Кузнецов",
        "created_at": "2023-07-30T11:00:00Z",
        "last_activity": "2024-01-19T13:25:00Z"
    },
    {
        "user_id": 1006,
        "username": "popova_anna",
        "first_name": "Анна",
        "last_name": "Попова",
        "created_at": "2023-09-18T08:45:00Z",
        "last_activity": "2024-01-18T10:15:00Z"
    },
    {
        "user_id": 1007,
        "username": "vasiliev_sergey",
        "first_name": "Сергей",
        "last_name": "Васильев",
        "created_at": "2023-12-01T15:30:00Z",
        "last_activity": "2024-01-22T17:40:00Z"
    },
    {
        "user_id": 1008,
        "username": "novikova_olga",
        "first_name": "Ольга",
        "last_name": "Новикова",
        "created_at": "2023-06-25T13:10:00Z",
        "last_activity": "2024-01-21T14:50:00Z"
    },
    {
        "user_id": 1009,
        "username": "fedorov_andrey",
        "first_name": "Андрей",
        "last_name": "Федоров",
        "created_at": "2023-10-12T10:20:00Z",
        "last_activity": "2024-01-17T12:35:00Z"
    },
    {
        "user_id": 1010,
        "username": "morozova_natalia",
        "first_name": "Наталья",
        "last_name": "Морозова",
        "created_at": "2024-01-08T09:05:00Z",
        "last_activity": "2024-01-22T15:20:00Z"
    }
]

export default function Login() {
    return (
        <div className="bg-background">
            <div className="flex flex-col">
                <button className="bg-primary text-text-on-primary font-medium
                px-6 py-3 rounded-4xl
                hover:shadow-2xl hover:bg-hover hover:text-text transition duration-150
                w-36 mt-2 ml-2 mb-10">
                    <Link href='/'>
                        Назад
                    </Link>
                </button>
                <TableUsers users={test_data} />
            </div>
        </div>
    );
}