import { createServer } from "./server.js"; // .js extension is required with NodeNext

const port = parseInt(process.env.PORT ?? "") || {{cookiecutter.service_port}};

const app = createServer();

const server = app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

server.on("error", (err) => {
  const error = err as NodeJS.ErrnoException;
  if (error.code === "EADDRINUSE") {
    console.error(
      `Port ${port} is already in use. Please use a different port or terminate the process using this port.`
    );
    // Optionally, you can try to use a different port or exit the process
    process.exit(1);
  } else {
    console.error("An error occurred:", err);
  }
});