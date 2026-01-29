'use client';

import Link from "next/link";
import TableUsers from "./TableUsers";
import { useState, useEffect } from "react";
import { getUsers, getUsersForChart } from "@/utils/api";
import Button from "@/components/ui/Button";
import UsersChart from "../components/UsersChart";

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

const test_users_for_chart = [
    {
        "total_quantity_of_users": 12,
        "timestamp": "2026-01-29T16:47:44.522200+07:00"
    },
    {
        "total_quantity_of_users": 19,
        "timestamp": "2026-01-29T16:48:44.522200+07:00"
    },
    {
        "total_quantity_of_users": 8,
        "timestamp": "2026-01-29T16:49:44.522200+07:00"
    },
    {
        "total_quantity_of_users": 15,
        "timestamp": "2026-01-29T16:50:44.522200+07:00"
    },
    {
        "total_quantity_of_users": 22,
        "timestamp": "2026-01-29T16:51:44.522200+07:00"
    },
    {
        "total_quantity_of_users": 18,
        "timestamp": "2026-01-29T16:52:44.522200+07:00"
    },
    {
        "total_quantity_of_users": 25,
        "timestamp": "2026-01-29T16:53:44.522200+07:00"
    }
];

export default function Info() {
    const [users, setUsers] = useState([]);
    const [loadingUsers, setLoadingUsers] = useState(true);

    const [usersForChart, setUsersForChart] = useState([]);
    const [loadingUsersForChart, setLoadingUsersForChart] = useState(true);

    async function loadUsers() {
        try {
            setLoadingUsers(true)
            const data = await getUsers();
            setUsers(data);
        } catch (err) {
            console.error('Fetch error:', err);
            setUsers(test_users);
        } finally {
            setLoadingUsers(false);
        }
    }

    async function loadUsersForChart() {
        try {
            setLoadingUsersForChart(true)
            const data = await getUsersForChart();
            setUsersForChart(data);
        } catch (err) {
            console.error('Fetch error:', err);
            setUsersForChart(test_users_for_chart);
        } finally {
            setLoadingUsersForChart(false);
        }
    }

    // Загрузка пользователей
    useEffect(() => {
        loadUsers();
    }, []);

    // Загрузка пользователей для графика
    useEffect(() => {
        loadUsersForChart();
    }, []);

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
                        {loadingUsers ? 'Загрузка...' : 'Обновить таблицу'}
                    </Button>
                </div>
                <TableUsers users={users} />
                <div
                    className="flex flex-row justify-between items-end
                    mx-[5%] mb-4 mt-10">
                    <h1 className="text-3xl text-foreground font-extrabold leading-none -mb-1.25">График пользователей</h1>
                    <Button
                        variant="primary"
                        onClick={loadUsersForChart}
                        additional="mr-[-1px]"
                    >
                        {loadingUsersForChart ? 'Загрузка... ' : 'Обновить график'}
                    </Button>
                </div>
                <UsersChart users={usersForChart} />
            </div>
        </div>
    );
}