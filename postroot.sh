pluginfoldername=$3

cp /opt/loxberry/data/plugins/$pluginfoldername/supervisor.conf /etc/supervisor/conf.d/smsgateway.conf
cp /opt/loxberry/data/plugins/$pluginfoldername/supervisorsend.conf /etc/superv
isor/conf.d/smsgatewaysend.conf
cp /opt/loxberry/data/plugins/$pluginfoldername/smsd.conf /etc/smsd.conf

/etc/init.d/smstools enable
/etc/init.d/smstools start

supervisorctl reread
supervisorctl start smsgateway
