'use client';

import { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js';

// Регистрация компонентов Chart.js
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

function formatDate(dateString) {
    const date = new Date(dateString);

    const day = date.getDate();
    const month = date.toLocaleDateString("ru-RU", { month: "long" });
    const year = date.getFullYear();

    return [' ' + day, ' ' + month, ' ' + year];
}

export default function UsersChart({ users }) {
    const [colors, setColors] = useState({
        primary: 'rgb(0, 0, 0)'
    });

    useEffect(() => {
        // Получение CSS-переменных из :root
        const root = document.documentElement;
        const primary = getComputedStyle(root)
            .getPropertyValue('--color-primarymuted300')
            .trim();

        setColors({
            primary: primary || 'rgb(0, 0, 0)'
        });
    }, []);

    const data = {
        labels: users.map(item => formatDate(item.timestamp)),
        datasets: [
            {
                label: 'Пользователи',
                data: users.map(item => item.total_quantity_of_users),
                borderColor: colors.primary,
                backgroundColor: colors.primary,
                tension: 0.35
            }
        ]
    };

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false,
            },
            tooltip: {
                callbacks: {
                    label: function (context) {
                        return `${context.dataset.label}: ${context.parsed.y} чел.`;
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Количество пользователей'
                },
                ticks: {
                    callback: function (value) {
                        return value + ' чел.';
                    },
                    stepSize: 1,
                    precision: 0
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Дата'
                }
            }
        }
    };

    return (
        <div>
            <div className="bg-background h-100 w-[90%] mx-[5%] border border-gray-200 rounded-2xl">
                <Line data={data} options={options} />
            </div>
        </div>
    );
}