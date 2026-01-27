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

export default function UsersChart() {
    const [colors, setColors] = useState({
        primary: 'rgb(75, 192, 192)'
    });

    useEffect(() => {
        // Получение CSS-переменных из :root
        const root = document.documentElement;
        const primary = getComputedStyle(root)
            .getPropertyValue('--color-primary')
            .trim();

        setColors({
            primary: primary || 'rgb(75, 192, 192)'
        });
    }, []);

    const testData = {
        labels: ['1 дек', '2 дек', '3 дек', '4 дек', '5 дек', '6 дек', '7 дек'],
        datasets: [
            {
                data: [12, 19, 8, 15, 22, 18, 25],
                borderColor: colors.primary,
                backgroundColor: colors.primary,
                tension: 0
            },
            // {
            //     data: [45, 52, 48, 55, 58, 52, 60],
            //     borderColor: 'rgb(255, 99, 132)',
            //     backgroundColor: 'rgba(255, 99, 132, 0.2)',
            //     tension: 0
            // }
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
                    }
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
                <Line data={testData} options={options} />
            </div>
        </div>
    );
}