import Link from "next/link";

export default function Login() {
    return (
        <div className="min-h-screen flex items-center justify-center flex-col bg-gray-50">
            <h1 className="text-3xl font-bold text-gray-900 mb-4">Форма входа</h1>
            <Link
                href='/'
                className="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition"
            >
                Назад
            </Link>
        </div>
    );
}