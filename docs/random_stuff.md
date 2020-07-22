# Random tips and tricks

## Copy large data:

### Use rsync or Globus?

As per William S. Monroe at Research Computing, Globus is the winner between the two:

> 1. If you’ve got more bandwidth, Globus gets faster (has some parallelism built in)
> 2. Globus is a managed transfer, so if there is a temporary interruption, it will pick back up
> 3. Like rsync, if you restart a transfer, it will just transfer over the stuff that has not yet successfully completed (though you can configure that)


### rsync command to copy large data

Command I used:

```sh
$ CLU="xxxx@cheaha.rc.uab.edu"
$ SOURCE_DIR="/Volumes/xxxx"
$ DEST_DIR="xxxx"
$ PARTIAL_DIR="${DEST_DIR}/.rsync-partial"
$ LOG_F="log.txt"

$ rsync --archive --human-readable --progress \
    -v -v \
    --partial-dir=$PARTIAL_DIR \
    --rsh=ssh \
    $SOURCE_DIR \
    $CLU:$DEST_DIR \
    >> $LOG_F
```

* [See here](https://serverfault.com/a/141778) for what `--archive` flag does.
* `--partial-dir` flag is to help with [resuming after interruption](https://unix.stackexchange.com/a/252969/339199).
