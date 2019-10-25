FROM jboss/wildfly

ADD calendar.war /opt/jboss/wildfly/standalone/deployments/

RUN /opt/jboss/wildfly/bin/add-user.sh admin Admin#2019 --silent

USER jboss

EXPOSE 8080

EXPOSE 9990

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0", "-b", "0.0.0.0"]
