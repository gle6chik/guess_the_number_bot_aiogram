'use client';

import Link from "next/link";
import TableUsers from "./TableUsers";
import { useState, useEffect } from "react";
import { getUsers } from "@/utils/api";
import Button from "@/components/ui/Button";
import UsersChart from "../components/UsersChart";
import { Users } from "lucide-react";

const test_users = [
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

const test_user_statistics = [
    {
        "user_id": 1001,
        "easy_games_played": 15,
        "medium_games_played": 8,
        "hard_games_played": 3,
        "total_games_played": 26,
        "easy_best_result": 120,
        "medium_best_result": 85,
        "hard_best_result": 40,
        "games_won": 18,
        "games_lost": 8,
        "winning_percentage": 69.23,
        "losing_percentage": 30.77,
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-22T14:45:00Z"
    },
    {
        "user_id": 1002,
        "easy_games_played": 5,
        "medium_games_played": 12,
        "hard_games_played": 10,
        "total_games_played": 27,
        "easy_best_result": 95,
        "medium_best_result": 78,
        "hard_best_result": 65,
        "games_won": 15,
        "games_lost": 12,
        "winning_percentage": 55.56,
        "losing_percentage": 44.44,
        "created_at": "2024-01-10T09:15:00Z",
        "updated_at": "2024-01-21T16:20:00Z"
    },
    {
        "user_id": 1003,
        "easy_games_played": 20,
        "medium_games_played": 5,
        "hard_games_played": 0,
        "total_games_played": 25,
        "easy_best_result": 150,
        "medium_best_result": 60,
        "hard_best_result": 0,
        "games_won": 18,
        "games_lost": 7,
        "winning_percentage": 72.00,
        "losing_percentage": 28.00,
        "created_at": "2024-01-05T11:00:00Z",
        "updated_at": "2024-01-20T12:30:00Z"
    },
    {
        "user_id": 1004,
        "easy_games_played": 0,
        "medium_games_played": 0,
        "hard_games_played": 0,
        "total_games_played": 0,
        "easy_best_result": 0,
        "medium_best_result": 0,
        "hard_best_result": 0,
        "games_won": 0,
        "games_lost": 0,
        "winning_percentage": 100.00,
        "losing_percentage": 100.00,
        "created_at": "2024-01-12T13:45:00Z",
        "updated_at": "2024-01-12T13:45:00Z"
    },
    {
        "user_id": 1005,
        "easy_games_played": 8,
        "medium_games_played": 15,
        "hard_games_played": 5,
        "total_games_played": 28,
        "easy_best_result": 110,
        "medium_best_result": 92,
        "hard_best_result": 55,
        "games_won": 22,
        "games_lost": 6,
        "winning_percentage": 78.57,
        "losing_percentage": 21.43,
        "created_at": "2024-01-08T14:20:00Z",
        "updated_at": "2024-01-19T10:15:00Z"
    },
    {
        "user_id": 1006,
        "easy_games_played": 3,
        "medium_games_played": 2,
        "hard_games_played": 1,
        "total_games_played": 6,
        "easy_best_result": 80,
        "medium_best_result": 50,
        "hard_best_result": 30,
        "games_won": 2,
        "games_lost": 4,
        "winning_percentage": 33.33,
        "losing_percentage": 66.67,
        "created_at": "2024-01-18T16:10:00Z",
        "updated_at": "2024-01-22T09:45:00Z"
    },
    {
        "user_id": 1007,
        "easy_games_played": 25,
        "medium_games_played": 18,
        "hard_games_played": 12,
        "total_games_played": 55,
        "easy_best_result": 145,
        "medium_best_result": 105,
        "hard_best_result": 88,
        "games_won": 38,
        "games_lost": 17,
        "winning_percentage": 69.09,
        "losing_percentage": 30.91,
        "created_at": "2024-01-02T08:30:00Z",
        "updated_at": "2024-01-22T18:00:00Z"
    },
    {
        "user_id": 1008,
        "easy_games_played": 10,
        "medium_games_played": 10,
        "hard_games_played": 10,
        "total_games_played": 30,
        "easy_best_result": 100,
        "medium_best_result": 80,
        "hard_best_result": 70,
        "games_won": 20,
        "games_lost": 10,
        "winning_percentage": 66.67,
        "losing_percentage": 33.33,
        "created_at": "2024-01-14T12:00:00Z",
        "updated_at": "2024-01-21T15:30:00Z"
    },
    {
        "user_id": 1009,
        "easy_games_played": 1,
        "medium_games_played": 0,
        "hard_games_played": 0,
        "total_games_played": 1,
        "easy_best_result": 65,
        "medium_best_result": 0,
        "hard_best_result": 0,
        "games_won": 0,
        "games_lost": 1,
        "winning_percentage": 0.00,
        "losing_percentage": 100.00,
        "created_at": "2024-01-20T17:45:00Z",
        "updated_at": "2024-01-20T18:20:00Z"
    },
    {
        "user_id": 1010,
        "easy_games_played": 12,
        "medium_games_played": 20,
        "hard_games_played": 15,
        "total_games_played": 47,
        "easy_best_result": 130,
        "medium_best_result": 115,
        "hard_best_result": 95,
        "games_won": 32,
        "games_lost": 15,
        "winning_percentage": 68.09,
        "losing_percentage": 31.91,
        "created_at": "2024-01-03T10:45:00Z",
        "updated_at": "2024-01-22T11:10:00Z"
    }
]

export default function Login() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true)

    async function loadUsers() {
        try {
            setLoading(true)
            const data = await getUsers();
            setUsers(data);
        } catch (err) {
            console.error('Fetch error:', err);
            setUsers(test_users);
        } finally {
            setLoading(false);
        }
    }

    // Загрузка пользователей
    useEffect(() => {
        loadUsers();
    }, [])

    return (
        <div className="bg-background">
            <div className="flex flex-col">
                <div className="m-3 flex flex-row gap-3">
                    <Link href='/'>
                        <Button variant="primary">
                            Назад
                        </Button>
                    </Link>
                </div>
                <div
                    className="flex flex-row justify-between items-end
                    mx-[5%] mb-4">
                    <h1 className="text-3xl text-foreground font-extrabold leading-none -mb-1.25">Пользователи</h1>
                    <Button
                        variant="primary"
                        onClick={loadUsers}
                        additional="mr-[-1px]"
                    >
                        {loading ? 'Загрузка...' : 'Обновить таблицу'}
                    </Button>
                </div>
                <TableUsers users={users} />
                <div
                    className="flex flex-row justify-between items-end
                    mx-[5%] mb-4 mt-10">
                    <h1 className="text-3xl text-foreground font-extrabold leading-none -mb-1.25">График пользователей</h1>
                    <Button
                        variant="primary"
                        additional="mr-[-1px]"
                    >
                        Обновить график
                    </Button>
                </div>
                <UsersChart />
            </div>
        </div>
    );
}