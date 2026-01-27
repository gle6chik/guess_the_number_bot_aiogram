import Link from 'next/link';
import Button from '@/components/ui/Button';

export default function Home() {
  return (
    <div className="max-h-screen flex justify-center bg-background">
      <div className="text-center mt-60">
        <h1 className="text-4xl font-bold text-text-primary mb-5">
          Админ-панель Telegram бота
        </h1>
        <p className="text-text-tertiary mb-8">
          Панель управления находится в разработке
        </p>
        <div>
          <Link href="/info">
            <Button variant="primary">
              Войти
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}