import nodemailer from 'nodemailer'

const transporter = nodemailer.createTransport({
  host: "smtp.gmail.com",
  port: 465,
  secure: true,
  pool: true,
  maxConnections: 5,
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASSWORD,
  },
});

export const sendEmail = async (to, code) => {
  try {
    await transporter.sendMail({
      from: process.env.EMAIL_USER,
      to,
      subject: 'Ylham tassyklama kodyňyz',
      html: `
      <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px;">
                <div style="max-width: 500px; margin: auto; background: white; padding: 30px; border-radius: 10px; text-align: center;">
                    
                    <h2 style="color: #333;">Tassyklama kody</h2>
                    
                    <p style="font-size: 16px; color: #555;">
                        Ylham platformasy tarapyndan ugradylan tassyklama kodyňyz:
                    </p>
                    
                    <div style="font-size: 34px; font-weight: bold; color: #2c7be5; margin: 20px 0; letter-spacing: 3px;">
                        ${code}
                    </div>
                    
                    <p style="font-size: 14px; color: #888;">
                        Bu kod <b>10 minutdan</b> soň güýjini ýitirer.
                    </p>
                </div>
            </body>
        </html>
      `,
    });
    return true;
  } catch (error) {
    console.error("Email error:", error);
    return false;
  }
};