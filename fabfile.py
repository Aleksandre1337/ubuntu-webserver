from fabric import Connection, task

@task
def web_setup(c, WEBURL, DIRNAME):
    print("###################################################################################")
    c.run("sudo apt install zip unzip -y")

    print("###################################################################################")
    print("Installing dependencies")
    print("###################################################################################")
    c.run("sudo apt install apache2 wget unzip -y")

    print("###################################################################################")
    print("Start & enable service.")
    print("###################################################################################")
    c.run("sudo systemctl start apache2")
    c.run("sudo systemctl enable apache2")

    print("###################################################################################")
    print("Downloading and pushing website to webservers.")
    print("###################################################################################")
    c.run(f"wget -O website.zip {WEBURL}")
    c.run("unzip -o website.zip")

    print("###################################################################################")
    with c.cd(DIRNAME.split(".")[0]):  # Change here, use the directory name without the .zip extension
        c.run("zip -r tooplate.zip * ")
        c.run(f"sudo mv tooplate.zip /var/www/html/")  # Use mv instead of put

    with c.cd("/var/www/html/"):
        c.run("sudo unzip -o tooplate.zip")

    c.run("sudo systemctl restart apache2")

    print("Website setup is done.")