const styles = {
    "primary": "inline-flex bg-primary rounded-2xl text-white text-lg font-bold py-2 px-5 hover:shadow-lg hover:bg-primary700 duration-150"
};

export default function Button({ children, variant, onClick, additional }) {
    return (
        <div className={styles[variant] + " " + additional}>
            <button onClick={onClick}>
                {children}
            </button>
        </div>
    );
}