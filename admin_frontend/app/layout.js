import "./globals.css";

export const metadata = {
  title: "Admin | Guess the Number",
  description: "Manage panel of the Telegram bot",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header>
          <div
            className="w-full h-32
            font-bold bg-primary
            flex justify-center items-center">
            <p className="text-7xl text-white">Угадай число</p>
          </div>
        </header>
        {children}
      </body>
    </html >
  );
}
