#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {
        char buf[1024];
        while (1) {
                int n, s = socket(AF_INET, SOCK_STREAM, 0);

                struct sockaddr_in srv;
                memset(&srv, 0, sizeof(srv));
                srv.sin_family = AF_INET;
                srv.sin_port = htons(10661);
                inet_pton(AF_INET, "127.0.0.1", &srv.sin_addr);
                connect(s, (struct sockaddr *)&srv, sizeof(srv));

                n = recv(s, buf, 1024, 0);
                buf[n] = '\0'; puts(buf);

                srand(time(NULL));
                n = sprintf(buf, "%f\n", 1.0/rand());
                send(s, buf, n+1, 0);

                n = recv(s, buf, 1024, 0);
                buf[n] = '\0'; puts(buf);

                close(s);
        }
}
